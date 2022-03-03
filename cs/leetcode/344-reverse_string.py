# https://leetcode.com/problems/reverse-string/

def reverseString(s: list[str]) -> None:
    left = 0
    right = len(s)-1

    while left < right:
        s[left],s[right] = s[right],s[left]
        left, right = left + 1, right -1
    print(s)

if __name__  == '__main__':
    result = reverseString(['h','e','l','l','o'])
    print(result)
