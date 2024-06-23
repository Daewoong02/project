# 프로젝트 문제 1번
input = [10, 40, 30, 60, 30]

def problem1(input):
    mean = 0
    sum_list = 0
    for i in range(len(input)):
        sum_list += input[i]
    mean = sum_list/len(input)
    
    median = 0
    input = sorted(input)
    n = len(input)
    median = input[n//2]

    result = [0,0]
    
    result[0] = mean
    result[1] = median
    return result

result = problem1(input)

assert result == [34, 30]
print("정답입니다.")
