def solution14(a, b):
    '''
    Args:
      a: list of numbers
      b: list of numbers
    Returns:
      找到有多少數字是b的公因數，又是a的公倍數
      例子：a = [2,4] b=[16,32,96]
      output = [4,8,16] -> 3
    '''
    result = []
    common_factor = find_common_factor(b)
    
    for factor in common_factor:
        condition = True
        for num_a in a:
            if factor%num_a != 0:
                condition = False
                break
        if condition:
            result.append(factor)
    return (result, len(result))

def find_common_factor(arr):
    '''
    回傳公因數
    '''
    common_factor = []
    for i in range(min(arr)):
        num = i+1
        condition = True
        for num_arr in arr:
            if num_arr%num != 0:
                condition = False
                break
        if condition:
            common_factor.append(num)
    return common_factor

# a, b = [2,4] , [16,32,96]
# print(solution14(a,b)) # ([4,8,16], 3)
