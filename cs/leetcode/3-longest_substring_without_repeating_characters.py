
# using set
def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0
    l,r,max = 0, 0, 0
    char_set = set()

    while r < len(s):
        print(r)
        r +=1
        



    # for right in range(len(s)):
        
    #     if s[right] in char_set:

    #         char_set.add(s[right])    
    #     result = len(char_set)
    # return result

# using dict
# def lengthOfLongestSubstring_dict(s: str) -> int:




if __name__ == '__main__':
    result = lengthOfLongestSubstring('asdf')
    print("result:",result)