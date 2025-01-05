def evenodd(n):
    if n ^1==n+1:
        return True
    else:
        return False
number=int(input("Enter a number:"))
if evenodd(number):
    print("The number is even")
else:
    print("The number is odd")