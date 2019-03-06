def solution05(arr, n):
    '''
    Args:
      arr: an 2D square-shaped array of numbers 二維
      n: n square-shaped array 
    Returns:
      absolute difference between the sums of the matrix's two diagonals
      對角線差的絕對值
    '''

    left_to_right = 0
    right_to_left = 0

    for i in range(n):
        for j in range(n):
            if i==j:
                left_to_right += arr[i][j]
            if (i+j)==(n-1):
                right_to_left += arr[i][j]
    return abs(left_to_right - right_to_left)