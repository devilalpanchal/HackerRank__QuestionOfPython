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
# Task
# The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

# Example

# The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

n = int(input())
    for i in range(0,n):
      print(i**2)



# 06
# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

# Task

# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
      
      def is_leap(year):
    leap = False
    
    # Write your logic here
    if ( year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0 ):
        return True 
    else :
        return False
    
    return leap

year = int(input())