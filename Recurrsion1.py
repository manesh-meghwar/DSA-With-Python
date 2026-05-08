# -------------- All about Recurrsion concepts ------------------------------


print("---------------------N Natural Numbers-------------------")
def PrintN(n):
    if n >0:
        PrintN(n-1)
        print(n, end=" ")
PrintN(5)
print()

print("---------------------N Natural Numbers in Reverse Order-------------------")

def PrintNRevrse(n):
    if n >0:
        print(n, end=" ")
        PrintNRevrse(n-1)
PrintNRevrse(5)
print()

print("---------------------N Natural Odd Numbers -------------------")

def printOddNum(n):
    if n >0:
        printOddNum(n-1)
        print(n*2-1, end=" ")
printOddNum(10)
print()

print("---------------------N Natural Even Numbers -------------------")

def printEvenNum(n):
    if n >0:
        printEvenNum(n-1)
        print(n*2, end=" ")
printEvenNum(8)
print()


print("---------------------N Natural Odd Numbers In Reverse Order-------------------")

def printOddNumReverse(n):
    if n >0:
        print(n*2-1, end=" ")
        printOddNumReverse(n-1)
printOddNumReverse(10)
print()

print("---------------------N Natural Even Numbers In Reverse Order-------------------")

def printEvenNumReverse(n):
    if n >0:
        print(n*2, end=" ")
        printEvenNumReverse(n-1)
printEvenNumReverse(8)
print()


# ------------------------------------------------------------------------------------------------------------


print("---------------------Sum of N Natural Numbers-------------------")

def SumOfN(n):
    if n == 0:
        return 0
    return n + SumOfN(n-1)
print(SumOfN(4))
print()



print("---------------------Sum of N Odd Numbers-------------------")

def SumOfNOdd(n):
    if n == 1:
        return 1
    return 2*n-1 + SumOfNOdd(n-1)
print(SumOfNOdd(4))
print()


print("---------------------Sum of N Even Numbers-------------------")

def SumOfNEven(n):
    if n == 1:
        return 2
    return 2*n + SumOfNEven(n-1)

print(SumOfNEven(4))
print()


print("---------------------Calculate the factorial of N-------------------")

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)
print("factorial of N = ", fact(5))
print()


print("---------------------Calculate the sum of squares of first N Numbers -------------------")

def sumNSquares(n):
    if n == 1:
        return 1
    return n*n + sumNSquares(n-1)
print("sum squares of N Numbers = ", sumNSquares(5))
print()