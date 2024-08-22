import re


def assess_password_strength(password):
    # Initialize variables to keep track of password characteristics
    length = len(password)
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[@$!%*?&]', password)

    # Determine password strength based on the criteria
    strength = 0
    if length >= 8:
        strength += 1
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    # Provide feedback based on strength
    feedback = ""
    if strength == 5:
        feedback = "Your password is very strong!"
    elif strength == 4:
        feedback = "Your password is strong, but could be stronger."
    elif strength == 3:
        feedback = "Your password is moderate. Consider adding more complexity."
    elif strength == 2:
        feedback = "Your password is weak. Add more elements like uppercase, numbers, or special characters."
    elif strength == 1:
        feedback = "Your password is very weak. It needs to be longer and more complex."
    else:
        feedback = "Your password does not meet any basic criteria. Please choose a stronger password."

    return {
        "strength_score": strength,
        "feedback": feedback
    }


# Example usage:
password = input("Enter your password: ")
result = assess_password_strength(password)
print(f"Strength Score: {result['strength_score']}/5")
print(f"Feedback: {result['feedback']}")
