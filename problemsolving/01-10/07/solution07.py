def solution(n):
    '''
    Args:
      n: number of floors
    Returns:
      for example if n = 4
      print out like below

         #
        ##
       ###
      ####

    '''

    for i in range(n):
        num = i+1
        print(" "*(n-num) + "#"*num)