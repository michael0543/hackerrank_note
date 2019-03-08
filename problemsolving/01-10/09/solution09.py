def solution09(arr):
    '''
    Args:
      arr: an array of numbers
    Returns:
      how many "maximum" number in array
    '''

    maximum = max(arr)
    count = 0

    for i in range(len(arr)):
        if arr[i]==maximum:
            count += 1

    return count

# test_arr = [3,2,1,3]
# print(solution09(test_arr)) # 2