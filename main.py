### SonarQube Demo Repository Setup
# This sample Python script is designed to demonstrate SonarQube integration with GitHub.

# Sample Python Function with a Code Smell (Unused variable)
def sample_function():
    unused_variable = 10  # SonarQube should flag this as an issue
    print("Hello, SonarQube!")

if __name__ == "__main__":
    sample_function()
