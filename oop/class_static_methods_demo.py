
class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# Example usage
if __name__ == '__main__': 
    sum_result = Calculator.add(7, 8)
    print(f"The sum is: {sum_result}")

    product_result = Calculator.multiply(5, 10)
    print(f"The product is: {product_result}")