def check_delimiters(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in pairs.values():  # Якщо символ є відкриваючою дужкою
            stack.append(char)
        elif char in pairs:  # Якщо символ є закриваючою дужкою
            if not stack or stack.pop() != pairs[char]:
                return f"{expression}: Несиметрично"

    if stack:
        return f"{expression}: Несиметрично"
    else:
        return f"{expression}: Симетрично"

# Для тестів:
# print(check_delimiters("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # Симетрично
# print(check_delimiters("( 23 ( 2 - 3);"))              # Несиметрично
# print(check_delimiters("( 11 }"))                     # Несиметрично
