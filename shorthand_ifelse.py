a=int(input("enter a value: "))
b=int(input("enter b value: "))

# shorthand if-else
print(f"{a} is biggest") if a>b else print("=") if a==b else print(f"{b} is biggest")