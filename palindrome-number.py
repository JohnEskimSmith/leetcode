"""
9. Palindrome Number
Easy

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

    For example, 121 is a palindrome while 123 is not.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.



Constraints:

    -231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?
"""

# 76 ms
def palindrome_number(x: int) -> bool:
    if x > 10:
        values = []
        while True:
            if x // 10:
                values.append(x % 10)
                x = x // 10
            else:
                values.append(x % 10)
                break
        return values == values[::-1]
    if 0 <= x <= 9:
        return True
    return False


if __name__ == '__main__':
    value = 101
    result = palindrome_number(101)
    print(value, result)