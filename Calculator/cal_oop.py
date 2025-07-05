
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self,  a, b):

        return a + b

    def subtract(self, a, b):
        
        return a - b

    def multiply(self, q, b):
        
        return q * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")

        return a / b

    def reset(self):
        self.result = 0
        return self.result
    


if __name__ == "__main__": 
    calc = Calculator()

    print("Calculator Module")
    print("Addition:", calc.add(5, 3))
    print("Subtraction:", calc.subtract(5, 3))
    print("Multiplication:", calc.multiply(5, 3))
    print("Division:", calc.divide(5, 3))
    print("Reset Result:", calc.reset())
    print("All operations completed successfully.")
else:
    print("Calculator Module imported successfully.")