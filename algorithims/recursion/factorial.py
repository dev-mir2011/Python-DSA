def factorial(num):
    if num == 0:
        return 1
    
    else:
        return num * factorial(num-1)
    


print(factorial(5)) # Return factorial of 5 which is 120