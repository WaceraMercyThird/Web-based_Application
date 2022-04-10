# import random

# Two ways to return one number in  an array 
# Strategy One
def max_num(num1, num2, num3):

    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2>= num1 and num2 >= num3:
        return num2
    elif num1 and num2 >= num3:
     return num2, 
    else: return num3


print(max_num(4, 40, 5))


# strategy 2
max_num = [4,40,5]               #Array of integers
max_num.sort(reverse=True)        # sorted in descending order
x = max_num[0]             
print(x)                          # returns first the one

