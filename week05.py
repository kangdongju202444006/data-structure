def is_valid_parentheses(expression: str) -> bool:
    stack = list()
    dic = {')': '(', '}': '{', ']': '['}  # 닫는 괄호 -> 여는 괄호 매핑

    for letter in expression:
        if letter in dic.values():  # 여는 괄호일 경우 스택에 추가
            stack.append(letter)
        elif letter in dic.keys():  # 닫는 괄호일 경우
            if not stack or stack.pop() != dic[letter]:  # 스택이 비었거나 매칭이 안 되면 False
                return False

    return not stack  # 스택이 비어 있으면 True, 아니면 False


# 테스트 케이스
print(is_valid_parentheses("[({1+2})]"))  # True
print(is_valid_parentheses(")(1+2))"))   # False
print(is_valid_parentheses("(1+2))"))    # False
print(is_valid_parentheses("(1+2)"))     # True
print(is_valid_parentheses("((3*2)/2)")) # True
