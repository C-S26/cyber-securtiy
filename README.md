Acknowledged. I will structure the repository content to focus on the setup, scanning process, and the logic of the patch without displaying the full code blocks directly in the response. This will encourage your mentees to clone the repository and interact with the code in their own environment.

Here is the GitHub-ready Markdown for this topic:

# 🛠️ Lab: Patch Management & Static Analysis with Bandit

This repository focuses on **Static Application Security Testing (SAST)**. You will use **Bandit**, a tool designed to find common security issues in Python code, to analyze a login script and then apply a "patch" to fix the vulnerabilities.

## 📋 Prerequisites

1. **Python 3.11** installed on your system.

2. **A Text Editor**: VS Code, Notepad++, or any editor of your choice.

3. **Install Bandit**: Open your terminal and run the following command:
```bash
pip install bandit
```

## 🚀 Hands-on Activity

### 1. Environment Setup

* **Clone the Repository**: Use `git clone` to pull this laboratory to your local machine.
* **Locate the Target**: Find the script named `app_login.py`. This file contains common security flaws, such as hardcoded credentials and unsafe file path handling.


### 2. Run the Security Scan

Open your terminal in the repository folder and execute a recursive scan to identify vulnerabilities:

```bash 
bandit -r .
```

### 3. Analyze the Findings
Review the Bandit output and focus on the following:
**Hardcoded Passwords**: Look for "Low", "Medium", or "High" severity alerts related to string literals used in authentication.
**Absolute Paths**: Notice how the script references local directories (like `E:\cybersecurity\`), which can expose system architecture to an attacker.

### 4. Apply the Patch
**Patch Management** is the practice of fixing these identified vulnerabilities to maintain system integrity.
**Task**: Modify the script to remove the plaintext password. Consider using a hashing algorithm or environment variables.
**Verify**: After applying your changes, run the Bandit scan again to ensure all "High" severity issues are resolved.

## 📖 Key Concepts Covered
**SAST (Static Analysis)**: Reviewing code for flaws without actually running it.
**Patch Management**: The lifecycle of identifying and deploying code updates to mitigate risks.
**Secure Authentication**: Moving away from hardcoded secrets toward secure storage methods.

