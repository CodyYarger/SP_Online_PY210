# 12/04/2020
# Dev: Cody Yarger
# lesson02: Fizz Buzz Function

# Write a program that prints the numbers from 1 to 100 inclusive.
# But for multiples of three print “Fizz” instead of the number.
# For the multiples of five print “Buzz” instead of the number.
# For numbers which are multiples of both three and five print “FizzBuzz” instead.

def fizz_buzz(n):
    """ This function iterates through a range of 1 to 100 and prints Fizz for
    numbers that are multiples of 3, Buzz for numbers that are multiples of 5 and
    FizzBuzz for numbers that are multiples of both 3 and 5."""

    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0: #if modulo of num and 3 and 5 = 0, print FizzBuzz
            print("FizzBuzz")
        elif num % 3 == 0:# if modulo of num and 3 = 0, print Fizz
            print("Fizz")
        elif num % 5 == 0: #if modulo of num and 5 = 0, print Buzz
            print("Buzz")
        else: print(str(num)) #if num is not a multiple of 3 or 5 print num.
