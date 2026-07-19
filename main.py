n=int(input("enter your number: "))
exponent=int(input("enter your exponent: "))
result=1
for i in range(exponent):
    result=result*n
print(f"{n} raised to the power {exponent} is:",result)