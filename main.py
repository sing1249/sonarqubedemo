### SonarQube Demo Repository Setup
# This sample Python script is designed to demonstrate SonarQube integration with GitHub.

# Sample Python Function with multiple issues
def sample_function():
    unused_variable = 10  # Unused variable (Code Smell)

    for i in range(5):  # Loop variable 'i' is never used (Code Smell)
        pass

    x = 1 / 0  # Division by zero (Bug)

    if True:  # Hardcoded condition (Code Smell)
        print("This is always executed.")

    print("Hello, SonarQube!")


def badly_named_function():  # Function name does not follow naming conventions
    a = "1"
    b = 1
    c = a + b  # Type mismatch: string + int (Bug)
    return c


if __name__ == "__main__":
    sample_function()
    badly_named_function()
