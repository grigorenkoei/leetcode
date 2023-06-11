class Solution:
    def threeSum(self, nums: list) -> list[list]:
        nums.sort()
        res = list()
        uniques = set()
        i = 0
        while i < len(nums) - 2:
            if nums[i] > 0:
                return res

            while i + 3 < len(nums) and nums[i + 3] == nums[i]:
                i += 1

            j = i + 1
            k = len(nums) - 1

            while k - 3 > j and nums[k - 3] == nums[k]:
                k -= 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if not s:
                    line = str(nums[i]) + str(nums[j]) + str(nums[k])
                    if line not in uniques:
                        res.append([nums[i], nums[j], nums[k]])
                        uniques.add(line)
                    j += 1
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
        return res