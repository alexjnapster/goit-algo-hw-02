from collections import deque
def is_palindrome(s):
    # Очищення рядка від пробілів та перетворення на нижній регістр
    s = ''.join(char.lower() for char in s if char.isalnum())

    # Створення deque з символів рядка
    d = deque(s)

    # Перевірка на паліндром
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False

    return True

# Для тестів:
#print(is_palindrome("A man, a plan, a canal, Panama"))  # True
#print(is_palindrome("No lemon, no melon"))             # True
#print(is_palindrome("Hello"))                          # False
