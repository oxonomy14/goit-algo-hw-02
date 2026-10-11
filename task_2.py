
from collections import deque


def is_palindrome(text):
   
    text = ''.join(text.lower().split())

   
    char_deque = deque(text)

   
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True


text = input("Введіть рядок: (наприклад, 'A man a plan a canal Panama') ")

if is_palindrome(text):
    print("Рядок є паліндромом.")
else:
    print("Рядок не є паліндромом.")
