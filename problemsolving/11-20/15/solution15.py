def solution15(scores):
    '''
    Args:
      scores: a list of scores 一連串的分數
    Returns:
      (max_socre, min_score)
      max_score 代表突破幾次最高分數
      min_score 代表突破幾次最低分數
    '''

    min_score = max_score = scores[0]
    min_count = max_count = 0

    for i in scores[1:]:
        if i > max_score:
            max_score = i
            max_count += 1
        elif i < min_score:
            min_score = i
            min_count += 1
    
    return (max_count, min_count)

scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
print(solution15(scores)) # (2, 4)