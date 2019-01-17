import collections


def finder2(arr1, arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


print(finder2([1, 2, 3, 4, 5], [1, 2, 4, 5]))