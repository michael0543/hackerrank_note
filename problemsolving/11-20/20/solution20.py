def solution20(bill, k, b):
    '''
    Args:
        bill: a list of bill number 一個list包含每道菜的價錢
        k: index which Anna doesn't eat 安娜不吃的菜的index
        b: Bob's calculation 包伯計算去除安娜不吃的菜後平分價錢
    Returns:
        if b is correct answer, return 'Bon Appetit'
        otherwise, calculate the difference between b and correct answer
        如果b是正確的平分價錢，則回傳'Bon Appetit'
        如果不是，則計算b與正確價錢的差並回傳
    '''

    total = sum(bill)
    result = int((total-bill[k])/2)
    if b == result: return 'Bon Appetit'
    else: return (b-result)

# bill, k, b = [3,10,2,9], 1, 12
# print(solution20(bill,k,b)) # 5
# bill, k, b = [3,10,2,9], 1, 7
# print(solution20(bill,k,b)) # Bon Appetit