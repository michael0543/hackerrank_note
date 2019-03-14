def solution13(x1, v1, x2, v2):
    '''
    Args:
      x1: position of A kangaroo
      x2: position of B kangaroo
      v1: speed of A kangaroo
      v2: speed of B kangaroo
    Return:
      'YES' if two kangaroos can meet in same point at same time
      'No' otherwise
    '''

    if v1 != v2:
        time = (x2-x1)/(v1-v2)
        if time > 0 and time == int(time):
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'

# x1, v1, x2, v2 = 0, 3, 4, 2
# print(solution13(x1, v1, x2, v2)) # YES