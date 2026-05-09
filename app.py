print("Welcome, you are in git project")

def add(a, b):
    return a + b

def greet(name):
    return f"Hello, {name}!"

def multiply(x, y):
    return x * y


greet("John")

add_result = add(70, 30)
print("The result of addition is:", add_result)

multiply_result = multiply(5, 4)
print("The result of multiplication is:", multiply_result)

print("New feature in progress")
def buggy_function():
    return 1/0
def correct_function():
    return 'This works correctly'
