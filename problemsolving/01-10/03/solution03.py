def solution03(a, b):
    '''
    Args:
      a: number of array for person a
      b: number of array for person b
    Returns:
      (num1, num2)
      num1: how many a[i] > b[i]
      num2: how many a[i] < b[i]
    '''

    point_a = 0
    point_b = 0

    if len(a) == len(b):
        for i in range(len(a)):
            item_a, item_b = a[i], b[i]

            if item_a > item_b: point_a += 1
            elif item_a < item_b: point_b += 1
            else: pass

    return (point_a, point_b)