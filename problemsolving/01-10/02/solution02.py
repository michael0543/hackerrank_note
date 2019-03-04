def solution02_2(arr):
    '''
    Args:
      arr: an array of numbers
    Returns:
      sum of the array
    '''

    result = 0
    count = 0

    while count != len(arr):
        result += arr[count]
        count += 1

    return result