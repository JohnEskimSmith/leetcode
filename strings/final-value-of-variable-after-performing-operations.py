"""
2011. Final Value of Variable After Performing Operations
Easy

There is a programming language with only four operations and one variable X:

    ++X and X++ increments the value of the variable X by 1.
    --X and X-- decrements the value of the variable X by 1.

Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.



Example 1:

Input: operations = ["--X","X++","X++"]
Output: 1
Explanation: The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.

Example 2:

Input: operations = ["++X","++X","X++"]
Output: 3
Explanation: The operations are performed as follows:
Initially, X = 0.
++X: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
X++: X is incremented by 1, X = 2 + 1 = 3.

Example 3:

Input: operations = ["X++","++X","--X","X--"]
Output: 0
Explanation: The operations are performed as follows:
Initially, X = 0.
X++: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
--X: X is decremented by 1, X = 2 - 1 = 1.
X--: X is decremented by 1, X = 1 - 1 = 0.



Constraints:

    1 <= operations.length <= 100
    operations[i] will be either "++X", "X++", "--X", or "X--".

"""
def final_value_of_variable_after_performing_operations(operations: list[str]) -> int:
    """
    :type operations: List[str]
    :rtype: int
    """
    x = 0
    return sum((x+1 for c in operations if '+' in c)) + sum((x-1 for c in operations if '-' in c))

    # for c in operations:
    #     if c=='++X' or c == 'X++':
    #         x += 1
    #     else:
    #         x -= 1
    # return x

    # return operations.count('X++')+operations.count('++X') - operations.count('X--') - operations.count('--X')

if __name__ == '__main__':
    result = final_value_of_variable_after_performing_operations(["X++", "++X", "--X", "X--"])
    print(result)

"""
Time Submitted
	
Status
	
Runtime
	
Memory
	
Language
03/14/2022 17:43	Accepted	67 ms	13.1 MB	python
"""