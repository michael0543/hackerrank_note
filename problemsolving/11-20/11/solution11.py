def solution11(grades):
    '''
    Args:
      grades: a list of students' grades
    Return:
      list of grades after rounding method
    
    ex_input = [73, 67, 38, 33]
    ex_output= [75, 67, 40, 33]
    '''

    results = []

    for i in range(len(grades)):

        if grades[i] < 40:
            if grades[i] >= 38:
                results.append(40)
            else:
                results.append(grades[i])
        else:
            num_five = (grades[i]//5)+1
            next_grade = num_five*5
            if (next_grade-grades[i])<3:
                results.append(next_grade)
            else:
                results.append(grades[i])

    return results

# ex_input = [73, 67, 38, 33]
# print(solution11(ex_input)) # ex_output= [75, 67, 40, 33]
