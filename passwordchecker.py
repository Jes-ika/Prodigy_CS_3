import re

def assess_password_strength(password):
    # Initialize score and feedback messages
    score = 0
    feedback = []
    
    # Criteria for a strong password
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    # Assess each criterion and provide feedback
    if length_criteria:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if uppercase_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")
    
    if lowercase_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")
    
    if number_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one number.")
    
    if special_char_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one special character (e.g., !@#$%^&*).")
    
    # Determine strength based on score
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"
    
    # Output password strength and feedback
    return {
        "password_strength": strength,
        "score": score,
        "feedback": feedback
    }

# Test example
password = input("Enter a password to check its strength: ")
result = assess_password_strength(password)

print(f"Password Strength: {result['password_strength']}")
print("Score:", result['score'], "/ 5")
if result['feedback']:
    print("Suggestions for improvement:")
    for suggestion in result['feedback']:
        print("-", suggestion)
