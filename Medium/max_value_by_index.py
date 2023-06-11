# nums index == target
class Solution:
    def calculate_sum(self, length, ind, max_el):
        num_left_el = min(ind + 1, max_el)
        first_cent_sum = max_el + (max_el - num_left_el + 1)
        left_sum = (first_cent_sum / 2) * num_left_el

        num_right_el = min(max_el, length - ind)
        right_central_sum = (max_el + (max_el - num_right_el + 1))
        right_sum = (right_central_sum / 2) * num_right_el
        return right_sum + left_sum - max_el + (length - (num_right_el + num_left_el - 1))

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left_b = 1
        right_b = maxSum
        if n == 1:
            return maxSum

        while left_b != right_b:
            max_el = (left_b + right_b) // 2
            curr_sum = self.calculate_sum(n, index, max_el)

            if curr_sum > maxSum:
                right_b = max_el

            elif curr_sum < maxSum:
                if right_b - left_b == 1:
                    return left_b
                left_b = max_el
            else:
                return max_el
