def solution19(year):
    '''
    Args:
        year: input an year
    Returns:
        output the 256th day in the input year in dd.mm.yyyy format
        1700-1917 leap year is that (year%4 == 0)
        1918-2700 leap year is that (year%400==0) or (year%4==0 and year%100!=0)
        1918 is a special year that the date after 1/31 is 2/14
        輸出為輸入那年第256天的日期，格式為 日期.月份.西元年份
        1700-1917年，閏年規則為 (year%4 == 0)
        1918-2700年，閏年規則為 (year%400==0) or (year%4==0 and year%100!=0)
        1918年1/31隔一天為2/14日
    '''

    if year < 1918:
        if year%4 == 0:
            date = '12.09.'+str(year)
        else:
            date = '13.09.'+str(year)
    elif year > 1918:
        if (year%400==0) or (year%4==0 and year%100!=0):
            date = '12.09.'+str(year)
        else:
            date = '13.09.'+str(year)
    else: # 1918 year 
        date = '26.09.'+str(year)

    return date

print(solution19(1918))
print(solution19(2017))
print(solution19(2016))