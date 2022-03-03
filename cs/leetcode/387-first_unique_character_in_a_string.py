#

# time complexity: O(N) go thru string of length N two times
# space complexity: O(1) bc English alphabet contains 26 letters
def firstUniqChar(s: str) -> int:
    char_set = {}
    for char in s:
        # print(char)
        # print(char_set)
        if char in char_set:
            char_set[char] += 1
        else:
            char_set[char] = 1
    print(char_set)
    for i,char in enumerate(s):
        if char_set[char] == 1:
            return i
    return -1
        

if __name__ == '__main__':
    result = firstUniqChar("dddccdbba")
    print(result)