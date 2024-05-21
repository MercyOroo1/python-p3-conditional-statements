#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if (username == "admin" or username == "ADMIN") and password == "12345" :
        print ("Access granted")
        return ("Access granted")
    else :
        print ("Access denied")
        return ("Access denied")

    pass 

def hows_the_weather(temperature):
    # your code here
    if (temperature < 40 ):
        print ("It's brisk out there!")
        return("It's brisk out there!")

    elif temperature <65 : 
        print ("It's a little chilly out there!")
        return("It's a little chilly out there!")

    elif  temperature > 85 :
        print ("It's too dang hot out there!")
        return ("It's too dang hot out there!")
    else :
        print ("It's perfect out there!")
        return ("It's perfect out there!")

    
    
    pass

def fizzbuzz(num):
    # your code here
    if (num%3 == 0 and num%5 == 0): 
        print ("FizzBuzz")
        return("FizzBuzz")
    elif num%5 == 0 :
        print ("Buzz")
        return ("Buzz")

    elif (num%3 == 0 ):
        print ("Fizz")
        return ("Fizz")
    else :
        print (num)
        return (num)
    pass


def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        print (num1 + num2)
        return (num1 + num2)
    elif operation == "-":
        print (num1 - num2)
        return (num1 - num2)
    elif operation == "*":
        print (num1 * num2)
        return (num1 * num2)
    elif operation == "/":
        print (num1/num2)
        return (num1/num2)
    else :
        print ("Invalid operation!")
        return None

    pass

calculator("+", 1, 1)
# 2
calculator("-", 3, 1)
# 2
calculator("*", 3, 2)
# 6
calculator("/", 4, 2)
# 2
calculator("nope", 4, 2)
# "Invalid operation!"
# None

