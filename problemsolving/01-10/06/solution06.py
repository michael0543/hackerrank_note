def solution06(arr):
    '''
    Args:
      arr: an array of numbers
    Returns:
      three numbers
      num1: portion of positive number in array
      num2: portion of negative number in array
      num3: portion of zeros in array
    '''

    count_positive = 0
    count_negative = 0
    count_zero = 0

    for i in range(len(arr)):
        if arr[i] > 0: count_positive += 1
        elif arr[i] < 0: count_negative += 1
        else: count_zero += 1

    return (count_positive, count_negative, count_zero)