def solution18(arr):
    '''
    Args:
        arr: a list of number, each number represents as one bird type
        每個數字都代表一種鳥的類型
    Returns:
        the number which occurs most
        if two numbers occur the same times, then return the small one
        出現最多次的數字，如果出現次數一樣多，則回傳較小的數字
    '''

    id_dict = {}

    for bird_id in arr:
        if bird_id not in id_dict:
            id_dict[bird_id] = 1
        else:
            id_dict[bird_id] += 1
    
    id_set = zip(id_dict.values(), id_dict.keys())
    max_value, max_key = 0, 0
    for id_ in id_set:
        if id_[0] > max_value:
            max_value, max_key = id_[0], id_[1]
        elif id_[0] == max_value:
            if id_[1] < max_key:
                max_key = id_[1]
    # return max_key,id_set
    return max_key

arr = [1,4,4,4,5,3]
print(solution18(arr)) #4