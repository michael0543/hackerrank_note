def solution17(k, arr):
    '''
    Args:
        k: target number
        arr: list of numbers
    Returns:
        how many pairs in list that match divisible situation
        situation: (arr[i] + arr[j]) % k == 0, i<j
        arr[i]+arr[j]可以被k整除
    '''
    count = 0
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            temp_num = arr[i]+arr[j]
            if temp_num%k == 0:
                count += 1
    return count

# k, arr = 3, [1,3,2,6,1,2]
# print(solution17(k,arr)) #5
