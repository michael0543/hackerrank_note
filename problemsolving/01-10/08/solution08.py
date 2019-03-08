def solution08(arr):
    '''
    Args:
      arr: an array of numbers
    Returns:
      two numbers
      num1: sum of array without maximum number
      num2: sum of array without minimum number
    '''

    total = sum(arr)
    maximum = max(arr)
    minimum = min(arr)

    return (total-maximum, total-minimum)

# test_arr = [1,3,5,7]
# print(solution08(test_arr))