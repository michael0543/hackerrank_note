def solution10(s):
    '''
    Args:
      s: str about time in 12-hour clock 
      example "07:05:45PM"
    Returns:
      time in 24-hour clock
      example "19:05:45"
    Notice:
      "12:00:00AM" -> "00:00:00"
      "12:00:00PM" -> "12:00:00"
    '''

    if s[-2:] == 'AM':
        if a[:2] == '12':
            out = '00' + s[2:-2]
        else:
            out = s[:-2]
    else:
        if s[:2] == '12':
            out = '12' + s[2:-2]
        else:
            out = str(int(s[:2])+12) + s[2:-2]

    return out

# test_s = '07:05:45PM'
# print(solution10(test_s)) # 19:05:45