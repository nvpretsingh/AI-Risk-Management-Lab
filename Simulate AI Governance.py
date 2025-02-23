# Simulate IAM Role-Based Access Control for AI Model
def check_user_access(user_role):
    allowed_roles = ["Data Scientist", "Security Analyst"]
    if user_role in allowed_roles:
        return "Access granted to AI model."
    else:
        return "Access denied! Unauthorized user."

# Example Usage
print(check_user_access("Intern"))  # Simulates unauthorized access attempt
print(check_user_access("Security Analyst"))  # Authorized user