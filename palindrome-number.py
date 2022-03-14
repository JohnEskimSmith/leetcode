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

"""
def palindrome_number(x: int) -> bool:
    if x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return True
    elif x > 10:
        values = []
        while True:
            if x // 10:
                values.append(x % 10)
                x = x // 10
            else:
                values.append(x % 10)
                break
        return values == values[::-1]
    else:
        return False

if __name__ == '__main__':
    print(palindrome_number(101))