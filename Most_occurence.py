from collections import Counter
def tester(arr):
    dict = {}
    # if len(arr) == 0:
    #     return ''
    #
    # if len(arr) == 1:
    #     for item in arr:
    #         dict[item] = 1
    #
    # # counter = 0
    # # arr.append(0)
    # # for i in range(1, len(arr)):
    # #     if arr[i - 1] == arr[i]:
    # #         counter += 1
    # #     else:
    # #         counter += 1
    # #         dict[arr[i - 1]] = counter
    # #         counter = 0
    # #
    # # return dict
    # # dict = {}
    # for i in range(len(arr)):
    #     if arr[i] in dict:
    #         dict[arr[i]] += 1
    #     else:
    #         dict[arr[i]] = 1

    dict = Counter(arr)
    print(dict)

    maxval = -99999
    maxkeypair = []
    for k, v in dict.items():
        if v > maxval:
            maxkeypair = [(k, v)]
            maxval = v
    print("%d is the most common value repeating %d times" % (maxkeypair[0][0],maxkeypair[0][1]))
    # s = max(y for x, y in dict.items())
    # print(sorted(dict.items(),key=lambda x: x[1],reverse=True)[0])

    # return s

# {'w':3, z :4 }





list = [5, 5, 5, 3, 5]
print(tester(list))

#for i in t_dict: