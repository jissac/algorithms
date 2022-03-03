# https://leetcode.com/problems/happy-number/

# convert number to string to get digits
def isHappy(n: int) -> bool:
    count = 0
    while n != 1:
        x = [int(a)**2 for a in str(n)]
        # print(x)
        n = sum(x)
        count += 1
        if count > 100000:
            return False
    return True

if __name__ == '__main__':
    num = 19
    result = isHappy(num)
    print(result)