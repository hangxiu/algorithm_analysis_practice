import numpy as np

hash_map = [x - x for x in np.arange(0, 6)]
# 实现数组的字典序
def Front_three_number_Dictionary_suqence(array, front_n, show):
    i = 0
    while i < front_n:
        while True:
            if hash_map[i] == 0:
                break
            else:
                i += 1
        if i != front_n:
            hash_map[i] = 1
            show.append(array[i])
            if (len(show) == front_n):
                print(show)
            Front_three_number_Dictionary_suqence(array, front_n, show)
            # if len(show) >= 1:
            del show[len(show) - 1]
            hash_map[i] = 0
        i += 1


def All_number_Dictionary_suqence(array, index, len_array, k, num):
    if k == num:
        result = []
        for i, data in enumerate(index):
            result.append(array[index[i]])
        print(result)
        return
    i = 0
    while i < len_array:
        if visit[i] == 0:
            index.append(i)
            visit[i] = 1
            k += 1
            All_number_Dictionary_suqence(array, index, len_array, k, num)
            del index[len(index) - 1]
            k -= 1
            visit[i] = 0
        i += 1


# 实现数组的排序 从小到大排序
def Array_index_from_small_to_big(array, start, result, count, num, arr_len):
    i = start
    while i < arr_len + 1 - count:
        result[count - 1] = i
        if count - 1 == 0:
            print_re = []
            for j, data in enumerate(result):
                print_re.append(array[result[j]])
            print_re.reverse()
            print(print_re)
        else:
            Array_index_from_small_to_big(array, i + 1, result, count - 1, num,
                                          arr_len)
        i += 1


# 实现数组的排序， 从大到小排序
def Array_index_from_big_to_small(array, start, result, count, num):
    i = start
    while i >= count:
        result[count - 1] = i - 1
        if count > 1:
            Array_index_from_big_to_small(array, i - 1, result, count - 1, num)
        else:
            print_re = []
            for j, data in enumerate(result):
                print_re.append(result[j])
            print_re.reverse()
            print(print_re)
        i -= 1


def Shift(n, i):
    result = []
    while i:
        remainder = i % 2
        i //= 2
        result.append(remainder)
    while len(result) < n:
        result.append(0)
    return result


def Mixed_Shift(n, i, m):
    result = []
    while i:
        remainder = i % m
        i //= m
        result.append(remainder)
    while len(result) < n:
        result.append(0)
    return result


def Mixed_Shift_Array(array_num, k, num, result):
    if k == num:
        print(result)
        return
    j = 0
    while j < len(array_num[k]):
        result[k] = array_num[k][j]
        Mixed_Shift_Array(array_num, k + 1, num, result)
        j += 1


if __name__ == "__main__":
    array = np.arange(0, 5)
    n = 3
    show = [x - x for x in range(0, n)]
    # test1 按系数从小到大排序
    # Array_index_from_small_to_big(array, 0, show, n, n, len(array))
#     Out_put
#     [0, 1, 2]
# [0, 1, 3]
# [0, 1, 4]
# [0, 2, 3]
# [0, 2, 4]
# [0, 3, 4]
# [1, 2, 3]
# [1, 2, 4]
# [1, 3, 4]
# [2, 3, 4]

    # test2 按系数从大到小排序
#     Array_index_from_big_to_small(array, len(array), show, n, n)
#     outPut
#     [4, 3, 2]
# [4, 3, 1]
# [4, 3, 0]
# [4, 2, 1]
# [4, 2, 0]
# [4, 1, 0]
# [3, 2, 1]
# [3, 2, 0]
# [3, 1, 0]
# [2, 1, 0]

    # test3 三个数的全排列
    # show1 = []
    # Front_three_number_Dictionary_suqence(array, n, show1)
    # outPUt
#     [0, 1, 2]
# [0, 2, 1]
# [1, 0, 2]
# [1, 2, 0]
# [2, 0, 1]
# [2, 1, 0]
    # test4 字典序
    # visit = [x - x for x in range(0, 5)]
    # index = []
    # All_number_Dictionary_suqence(array, index, len(array), 0, n)
    # output
#     [0, 1, 2]
# [0, 1, 3]
# [0, 1, 4]
# [0, 2, 1]
# [0, 2, 3]
# [0, 2, 4]
# [0, 3, 1]
# [0, 3, 2]
# [0, 3, 4]
# [0, 4, 1]
# [0, 4, 2]
# [0, 4, 3]
# [1, 0, 2]
# [1, 0, 3]
# [1, 0, 4]
# [1, 2, 0]
# [1, 2, 3]
# [1, 2, 4]
# [1, 3, 0]
# [1, 3, 2]
# [1, 3, 4]
# [1, 4, 0]
# [1, 4, 2]
# [1, 4, 3]
# [2, 0, 1]
# [2, 0, 3]
# [2, 0, 4]
# [2, 1, 0]
# [2, 1, 3]
# [2, 1, 4]
# [2, 3, 0]
# [2, 3, 1]
# [2, 3, 4]
# [2, 4, 0]
# [2, 4, 1]
# [2, 4, 3]
# [3, 0, 1]
# [3, 0, 2]
# [3, 0, 4]
# [3, 1, 0]
# [3, 1, 2]
# [3, 1, 4]
# [3, 2, 0]
# [3, 2, 1]
# [3, 2, 4]
# [3, 4, 0]
# [3, 4, 1]
# [3, 4, 2]
# [4, 0, 1]
# [4, 0, 2]
# [4, 0, 3]
# [4, 1, 0]
# [4, 1, 2]
# [4, 1, 3]
# [4, 2, 0]
# [4, 2, 1]
# [4, 2, 3]
# [4, 3, 0]
# [4, 3, 1]
# [4, 3, 2]

# test5 Shift 2进制数转换
# i = 18
# n = 10
# result = Shift(n, i)
# result.reverse()
# print(result)
# out_put
# [0, 0, 0, 0, 0, 1, 0, 0, 1, 0]

# test6 Mixed_Shift 任意进制转化
# i = 18
# n = 10
# m = 3
# result = Mixed_Shift(n, i, m)
# result.reverse()
# print(result)
# outPut
# [0, 0, 0, 0, 0, 0, 0, 2, 0, 0]

# test7 Mixed_Shift_Array 混合进制转化
# array = [3, 2, 3, 3]
# Scope = []
# for i in array:
#     Scope.append(i - 1)
# visit1 = []
# for i in range(0, len(Scope)):
#     sub_visit = [x for x in range(0, Scope[i] + 1)]
#     visit1.append(sub_visit)
# result = [x-x-1 for x in range(0, len(Scope))]
# Mixed_Shift_Array(visit1, 0, len(array), result)
# outPut
#     [0, 0, 0, 0]
# [0, 0, 0, 1]
# [0, 0, 0, 2]
# [0, 0, 1, 0]
# [0, 0, 1, 1]
# [0, 0, 1, 2]
# [0, 0, 2, 0]
# [0, 0, 2, 1]
# [0, 0, 2, 2]
# [0, 1, 0, 0]
# [0, 1, 0, 1]
# [0, 1, 0, 2]
# [0, 1, 1, 0]
# [0, 1, 1, 1]
# [0, 1, 1, 2]
# [0, 1, 2, 0]
# [0, 1, 2, 1]
# [0, 1, 2, 2]
# [1, 0, 0, 0]
# [1, 0, 0, 1]
# [1, 0, 0, 2]
# [1, 0, 1, 0]
# [1, 0, 1, 1]
# [1, 0, 1, 2]
# [1, 0, 2, 0]
# [1, 0, 2, 1]
# [1, 0, 2, 2]
# [1, 1, 0, 0]
# [1, 1, 0, 1]
# [1, 1, 0, 2]
# [1, 1, 1, 0]
# [1, 1, 1, 1]
# [1, 1, 1, 2]
# [1, 1, 2, 0]
# [1, 1, 2, 1]
# [1, 1, 2, 2]
# [2, 0, 0, 0]
# [2, 0, 0, 1]
# [2, 0, 0, 2]
# [2, 0, 1, 0]
# [2, 0, 1, 1]
# [2, 0, 1, 2]
# [2, 0, 2, 0]
# [2, 0, 2, 1]
# [2, 0, 2, 2]
# [2, 1, 0, 0]
# [2, 1, 0, 1]
# [2, 1, 0, 2]
# [2, 1, 1, 0]
# [2, 1, 1, 1]
# [2, 1, 1, 2]
# [2, 1, 2, 0]
# [2, 1, 2, 1]
# [2, 1, 2, 2]
