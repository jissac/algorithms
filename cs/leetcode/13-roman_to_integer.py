# https://leetcode.com/problems/roman-to-integer/submissions/
''' 
KEY INSIGHTS: read the problem carefully to recognize shortcuts - 
if letter/number on right is larger, always subtract
dictionary key-value makes it easier to compare letters and values
''' 

def romanToInt(s: str) -> int:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    for i,letter in enumerate(s):
        if (i != len(s)-1) and (roman_dict[s[i+1]] > roman_dict[letter]):
            print('yes')
            sum -= roman_dict[letter]
        else:
            sum += roman_dict[letter]
    return sum

if __name__ == '__main__':
    result = romanToInt('IV')
    print(result)