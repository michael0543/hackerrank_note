def solution12(s, t, a, b, apples, oranges):
    '''
    Args:
      s: 房子的左側數線位子
      t: 房子的右側數線位子
      a: 蘋果樹數線位子
      b: 橘子樹數線位子
      apples: list of 蘋果落下的距離
      oranges: list of 橘子落下的距離
    Returns:
      兩個數子，分別代表有幾個蘋果落入房子區間，分別代表有幾個橘子落入房子區間
    '''
    count_apple, count_orange = 0, 0
    # apple
    for i in range(len(apples)):
        d = a + apples[i]
        if d>=s and d<=t: count_apple += 1
    # orange
    for j in range(len(oranges)):
        d = b + oranges[j]
        if d>=s and d<=t: count_orange += 1

    return (count_apple, count_orange)

# li_apples = [-2, 2, 1]
# li_oranges = [5, -6]
# print(solution12(7, 11, 5, 15, li_apples, li_oranges)) #(1,1)