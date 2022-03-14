"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".



Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0



Constraints:

    1 <= jewels.length, stones.length <= 50
    jewels and stones consist of only English letters.
    All the characters of jewels are unique.


"""


#24 ms
def jewels_and_stones_1(jewels: str, stones: str) -> int:
    return sum(1 for s in stones if s in jewels)


# 49 ms
def jewels_and_stones_2(jewels: str, stones: str) -> int:
    value = 0
    for j in jewels:
        i = 0
        size = len(stones)
        while i < size:
            if j == stones[i]:
                size -= 1
                value += 1
                stones = stones[:i]+stones[i+1:]
                i -= 1
            i += 1
    return value


if __name__ == '__main__':
    result = jewels_and_stones_2(jewels = "aA", stones = "aAAbbbb")
    print(result)
    result = jewels_and_stones_2(jewels = "z", stones = "ZZ")
    print(result)

    result = jewels_and_stones_1(jewels = "aA", stones = "aAAbbbb")
    print(result)
    result = jewels_and_stones_1(jewels = "z", stones = "ZZ")
    print(result)
