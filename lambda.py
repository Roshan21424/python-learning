"""
lambda functions are anonymous and nameless functions used for:
1) small, single-expression logic
2) passing functions as arguments to other functions
"""

# lambda function
fun1 = lambda x: x ** 2

# passing lambda as argument
def fun2(lambdafun, n):
    return lambdafun(n)

if __name__ == "__main__":
    print(fun1(10)) # 100
    print(fun2(fun1, 10))  # 100
