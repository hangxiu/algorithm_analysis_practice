import numpy as np
import time

np.random.seed(0)
big_num = int(1e6)
num_set = np.random.randint(0, big_num, big_num)


# 以集合尾元素（或首元素）为主元，以下代码以尾元素为主元
def Partion(num_set, start, end):
    
    x = num_set[end]
    i = start - 1
    for j in range(start, end):
        if num_set[j] <= x:
            ++i
            num_set[i],num_set[j] = num_set[j], num_set[i]
    num_set[i+1], num_set[end] = num_set[end], num_set[i+1]
    return i + 1
def Partion2(num_set, start, end):
    if start > end:
        return
    tem = num_set[start]
    i, j = start, end
    while i != j:
        while num_set[j] >= tem and i < j:
            j -= 1
        while num_set[i] <= tem and i < j:
            i += 1
        if i < j:
            num_set[i], num_set[j] =  num_set[j], num_set[i]

        num_set[start], num_set[i] =  num_set[i], tem 
    
    return i
        
def qSort(num_set, start, end):
    if start < end:
        pos = Partion2(num_set, start, end)
        qSort(num_set, start, pos - 1)
        qSort(num_set, pos+1, end)

def FindMedian(num_set, pos1, pos2, pos3):
    if num_set[pos1] <= num_set[pos2] and num_set[pos1] <= num_set[pos3]:
        if num_set[pos2] <= num_set[pos3]:
            return pos2
        else:
            return pos3
    elif num_set[pos2] <= num_set[pos1] and num_set[pos2] <= num_set[pos3]:
        if num_set[pos1] <= num_set[pos3]:
            return pos1
        else:
            return pos3
    else:
        if num_set[pos1] <= num_set[pos2]:
            return pos1
        else:
            return pos2

def rand_Partion(num_set, start, end):
    num1 = num_set[np.random.randint(start, end)]
    num2 = num_set[np.random.randint(start, end)]
    num3 = num_set[np.random.randint(start, end)]
    
    pos = FindMedian(num_set, num1, num2, num3)
    num_set[end], num_set[pos] = num_set[pos], num_set[end]
    return Partion2(num_set, start, end)

def rand_qSort(num_set, start, end):
    if start < end:
        pos = rand_Partion(num_set, start, end)
        rand_qSort(num_set, start, pos-1)
        rand_qSort(num_set, pos+1, end)

# 快速排序的尾递归：
def qSort_tail(num_set, start, end):
    while start < end:
        pos = Partion2(num_set, start, end)
        qSort_tail(num_set, start, pos-1)
        start = pos + 1

# 快速排序的尾递归：
def qSort_tail_rand(num_set, start, end):
    while start < end:
        pos = rand_Partion(num_set, start, end)
        qSort_tail_rand(num_set, start, pos-1)
        start = pos + 1

if __name__ == "__main__":

    # Start_time = time.time()
    # # test1 常规快速排序
    # qSort(num_set, 0, len(num_set) - 1)
    # print("qSrot 的运算时间为：%g" %(time.time() - Start_time))

    # num_set = np.random.randint(0, big_num, big_num)
    # Start_time = time.time()
    # # test2 随机3个数选取快速排序
    # rand_qSort(num_set, 0, len(num_set) - 1)
    # print("rand_qSrot 的运算时间为：%g" %(time.time() - Start_time))


    num_set = np.random.randint(0, big_num, big_num)
    Start_time = time.time()
    # test3 常规快速排序尾递归
    qSort_tail(num_set, 0, len(num_set) - 1)
    print("一百万数据排序 tail_qSrot 的运算时间为：%g" %(time.time() - Start_time))
    # print("10万数据排序 tail_rand_qSrot 的运算时间为：%g" %(time.time() - Start_time))
    # print("一万数据排序 tail_rand_qSrot 的运算时间为：%g" %(time.time() - Start_time))
    # 一万数据排序 tail_qSrot 的运算时间为：0.445835
    # 10万数据排序 tail_qSrot 的运算时间为：40.2962
    #一百万数据排序 tail_qSrot 的运算时间为：3610.69


    num_set = np.random.randint(0, big_num, big_num)
    Start_time = time.time()
    # test4 随机3个数选取快速排序尾递归
    qSort_tail_rand(num_set, 0, len(num_set) - 1)
    print("一百万数据排序 tail_rand_qSrot 的运算时间为：%g" %(time.time() - Start_time))
    # print("10万数据排序 tail_rand_qSrot 的运算时间为：%g" %(time.time() - Start_time))
    # print("一万数据排序 tail_rand_qSrot 的运算时间为：%g" %(time.time() - Start_time))
    # 一万数据排序 tail_rand_qSrot 的运算时间为：0.685141
    # 10万数据排序 tail_rand_qSrot 的运算时间为：33.0446
    # 一百万数据排序 tail_rand_qSrot 的运算时间为：9245.72
    





