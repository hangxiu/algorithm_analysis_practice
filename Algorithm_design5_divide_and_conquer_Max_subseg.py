
def max_Sum_SubSeg(list, start, end):
    if start == end:
        if list[start] > 0:
            return list[start]
        else:
            return 0
    mid = (start + end) // 2
    MaxLeftSumSeg = max_Sum_SubSeg(list, start, mid)
    MaxRightSumSeg = max_Sum_SubSeg(list, mid + 1, end)

    leftMaxMerge, leftSum, rightMaxMerge, rightSum = 0,0,0,0
    i = mid
    while i >=0 :
        leftSum += list[i]
        if leftSum > leftMaxMerge:
            leftMaxMerge = leftSum
        i -= 1
    
    for i in range(mid + 1, end + 1):
        rightSum += list[i]
        if rightSum > rightMaxMerge:
            rightMaxMerge = rightSum
    
    MaxMerge = leftMaxMerge + rightMaxMerge
    reMax = MaxLeftSumSeg
    if reMax < MaxRightSumSeg:
        reMax = MaxRightSumSeg
    if reMax < MaxMerge:
        reMax = MaxMerge
    
    return reMax

if __name__ == "__main__":
    list = [4, -3, 5, -2, -1, 2, 6, -2]
    print("result %g" %max_Sum_SubSeg(list, 0, len(list) - 1))


