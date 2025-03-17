### SonarQube Demo Repository Setup
# This Python script demonstrates a clean implementation for SonarQube integration with GitHub.

def greet_sonarqube():
    """Prints a greeting message."""
    print("Hello, SonarQube!")


def safe_division(a: float, b: float) -> float:
    """Performs division safely, handling division by zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")  # Proper error handling
    return a / b


def sum_numbers(a: int, b: int) -> int:
    """Returns the sum of two integers."""
    return a + b


if __name__ == "__main__":
    greet_sonarqube()
    
    try:
        result = safe_division(10, 2)
        print(f"Division result: {result}")
    except ValueError as e:
        print(f"Error: {e}")

    total = sum_numbers(5, 7)
    print(f"Sum of numbers: {total}")


