class Node:
    def __init__(self, val=0, snap_id=-1):
        self.snap_id = snap_id
        self.val = val


class SnapshotArray:
    def __init__(self, length: int):
        self.values = dict()
        self.max_snap_id = -1
        self.index_changed = set()

    def set(self, index: int, val: int) -> None:
        lst = self.values.get(index, None)
        self.index_changed.add(index)
        if lst is None:
            lst = list()
            el = Node(val)
            if self.max_snap_id >= 0:
                lst.append(Node(0, 0))
            lst.append(el)
            self.values[index] = lst
        else:
            lst[-1].val = val

    def snap(self) -> int:
        self.max_snap_id += 1
        for i in self.index_changed:
            lst = self.values[i]
            node = lst[-1]
            node.snap_id = self.max_snap_id
            lst.append(Node())
        self.index_changed.clear()
        return self.max_snap_id

    def get(self, index: int, snap_id: int) -> int:
        lst = self.values.get(index, None)
        if lst is None:
            return 0
        else:
            l_border = 0
            r_border = len(lst)
            while l_border < r_border:
                mid = (l_border + r_border) // 2
                if lst[mid].snap_id > snap_id or lst[mid].snap_id == -1:
                    r_border = mid
                elif lst[mid].snap_id < snap_id:
                    if l_border == mid:
                        return lst[mid].val
                    l_border = mid
                else:
                    return lst[mid].val
        return lst[mid].val