# z = int(input())
# if z % 2 == 0:
#     print("z is even")
# else:
#     print("z is odd")



# Task
# Given an integer, , perform the following conditional actions:


# 02 of hacker rank
# If n is odd, print Weird
# If n is even and in the inclusive range of  to , print Not Weird
# If n is even and in the inclusive range of  to , print Weird
# If n is even and greater than , print Not Weird


n = int(input())
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0:
    if n >= 2 and n <= 5:
        print("Not Weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    elif n >20:
        print("Not Weird")

        

# 03
# Task
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# a = int(input())
# b = int(input())
        

a= 5
b= 5
print(a+b)    
print(a-b)   
print(a*b) 



# 04
# Task
# The provided code stub reads two integers,  and , from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .
# No rounding or formatting is necessary.
# Example
# The result of the integer division .
# The result of the float division is .

a = int(input())
b = int(input())
c = int(a//b)
d = float(a/b)
print(c)
print(d)



# 05

