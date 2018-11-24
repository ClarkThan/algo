# -*- coding: utf-8 -*-
ls1 = list(range(1000000)); ls1[0:3] = [1,0,1]
ls2 = list(range(1000000, 3000, -1)) + list(range(3000))


def find_index(lst):
    """
    一个无序大数组，相邻元素都不同，找出一个比左右相邻元素都小的元素的位置（如果是最两侧的元素，只要小于相邻元素也算）
    按照约定条件给出的参数数组，可以判断出数组中一定存在目标元素。
    首先判断左右两侧的元素是否满足，如果不满足则选择数组的二分点（中点）来进行判断：
    如果中点与相邻左右两点呈V字型，则直接返回该中点位置；如果呈`/`型则判断数组的左半部分一定存在目标点；如果呈`\`型则判断数组的左半部分一定存在目标点
    按如上方法不断查找
    :param lst:
    :return:
    >>> find_index(ls1)
    1
    >>> find_index(ls2)
    997000
    >>> find_index([2,1,2])
    1
    >>> find_index([1,2,1])
    0
    >>> find_index([1,3,5])
    0
    >>> find_index([5,4,3,2,1])
    4
    """

    length = len(lst)
    if length == 0:
        raise Exception('空数组')
    elif length == 1:
        return 0
    elif lst[1] > lst[0]:  # 检查最左边
        return 0
    elif lst[-2] > lst[-1]:  # 检查最右边
        return length - 1
    else:
        hd, tl = 0, length - 1
        while hd < tl:
            mid = (hd + tl) // 2  # 中位点
            left, cur, right = lst[mid-1], lst[mid], lst[mid+1]
            if left > cur:
                if right > cur:  # V字型
                    return mid
                else:  # 反斜线型 右半部分一定存在目标点
                    hd = mid
                    continue
            else:  # 斜线型 左半部分一定存在目标点
                tl = mid
                continue


if __name__ == '__main__':
    assert find_index(ls1) == 1
    assert find_index(ls2) == 997000
    assert find_index([2,1,2]) == 1
    assert find_index([1,2,1]) == 0
    assert find_index([1,3,5]) == 0
    assert find_index([5,4,3,2,1]) == 4
    print('test ok')
