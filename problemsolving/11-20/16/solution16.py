def solution16(s, d, m):
    '''
    Args:
        s: a list of numbers 代表每個巧克力上的數字
        d: day of the birthday date 生日日期中的日
        m: month of the birthday date 生日日期中的月
    Returns:
        check chocolates match the input birthday date
        len(slice of chocolate)==m , sum(slice of chocolate)==d
        例子：s=[1,2,1,3,2]  d=3  m=2
            s[0]+s[1]==3
            s[1]+s[2]==3
            return 2
    '''

    count = 0

    for i in range(0, len(s)-m+1):
        check_li = s[i:i+m]
        if sum(check_li)==d:
            count += 1
    return count

# s, d, m = [1,2,1,3,2], 3, 2
# print(solution16(s,d,m)) # 2
