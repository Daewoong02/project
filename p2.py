# 프로젝트 문제 2번
input = ")))()"

def problem2(input):
    result = 0
    stack = []
    for char in input:
        if char == "(":
            stack.append(char)
        else:
            if stack and stack[-1] == "(":
                stack.pop()
            elif not stack:
                result += 1
    result += len(stack)
    print(char)
    return result

result = problem2(input)

assert result == 3
print("정답입니다.")
