def solution02_1(arr):
    '''
    Args:
      arr: an array of numbers
    Returns:
      sum of the array
    '''

    result = 0

    for i in range(len(arr)):
        result += arr[i]

    return result