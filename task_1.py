
n1 = int(input("Please enter the number: "))
def factorial(n1):

    if n1 < 2 :
        return 1
    else:
        return n1 * factorial(n1 - 1)
result =  factorial(n1)
print("Factorial of",n1,"is:",result)

