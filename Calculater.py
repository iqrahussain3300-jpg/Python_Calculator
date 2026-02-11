def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiplication(a,b):
    return a * b
def division(a,b):
    if b == 0:
        print("Error! Division by zero not allowed")
    else:
        return a / b
print("Calculater.py __name__ is ", __name__)

if __name__ == "__main__":
    print("Testing Calculator functions")
    print(add(2,3))
    print(subtract(5,2))
    print(multiplication(4,3))
    print(division(10,2))
        
