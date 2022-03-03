
# https://leetcode.com/problems/fizz-buzz/solution/

# approach 1: modulo to check divisibility, most stringent condition first
# Time: O(N) , Space: O(1)
def fizzBuzz(n: int) -> list[str]:
    answer = []
    for i in range(1,n+1):
        if (i%3 == 0) and (i%5 == 0):
            answer.append('FizzBuzz')
        elif (i%3 == 0):
            answer.append('Fizz')
        elif (i%5 == 0):
            answer.append('Buzz')
        else:
            answer.append(str(i))
    return answer

# approach 2: instead of checking every combination, check for divisibility
# by given numbers in the problem

def fizzBuzzJazz(n: int) -> list[str]:
    answer = []
    for num in range(1,n+1):
        div_by_3 = (num % 3 == 0)
        div_by_5 = (num % 5 == 0)
        print(num)

        num_ans_str = ""
        if div_by_3:
            print("div3")
            num_ans_str += "Fizz"
        if div_by_5:
            print("div5")
            num_ans_str += "Buzz"
        if not num_ans_str: 
            num_ans_str = str(num)
            
        answer.append(num_ans_str)
    return answer

if __name__ == '__main__':
    result1 = fizzBuzz(15)
    result2 = fizzBuzzJazz(15)
    print(result1,result2)