# SonarQube Demo - Group 9

## Overview

**SonarQube** is a powerful tool that helps identify issues in code, such as bugs, vulnerabilities, and code smells. By using SonarQube, we ensure that our code follows best practices and meets quality standards.

### Key Components of the Repository

1. **`main.py`**: The Python script that contains the sample function, demonstrating both poor and clean coding practices. SonarQube will analyze this file for issues like unused variables, hardcoded conditions, type mismatches, and bugs.

2. **`sonar-project.properties`**: This file is used to configure SonarQube for the project. It contains important settings like:
    - **`sonar.projectKey`**: A unique key for the project.
    - **`sonar.organization`**: The organization on SonarCloud.
    - **`sonar.sources`**: Specifies the source files that SonarQube will analyze.

3. **`.github/workflows/sonar.yaml`**: The GitHub Actions workflow configuration file that sets up the automated SonarQube analysis. This file tells GitHub Actions to run SonarQube scanning whenever there is a push or pull request to the `main` branch.

4. **`sonar-project.properties`** (in the root directory): This configuration file tells SonarQube how to analyze the project. You can customize settings like the project key, sources, and encoding.

5. **SonarCloud Integration**: The repository is linked to SonarCloud, where the results of the code analysis are displayed. SonarCloud will provide feedback on code quality, identifying issues such as bugs, vulnerabilities, and code smells.

## How SonarQube Works

1. **SonarQube Analysis**: 
   - The Python script (`main.py`) is checked for issues like unused variables, hardcoded conditions, and type mismatches.
   - When SonarQube runs, it analyzes the source code and identifies issues based on the rules defined by SonarCloud.

2. **GitHub Actions Workflow**:
   - Every time there is a **push** or **pull request** to the `main` branch, the GitHub Actions workflow triggers and runs the SonarQube analysis automatically.
   - The configuration in **`.github/workflows/sonar.yaml`** ensures that SonarQube scans the code and reports any issues to SonarCloud.

3. **Quality Gate**:
   - SonarQube uses a **Quality Gate** to determine if the code meets the required quality standards. If issues are detected (such as bugs or code smells), the **Quality Gate** will fail, and you will see the results on **SonarCloud**.

4. **SonarCloud Dashboard**:
   - After each analysis, the results are uploaded to **SonarCloud**, where you can view detailed feedback on code quality.
   - You can see issues like:
     - **Bugs**: Errors that affect the functionality of the code.
     - **Code Smells**: Practices that make the code harder to maintain or understand.
     - **Vulnerabilities**: Security risks in the code.
