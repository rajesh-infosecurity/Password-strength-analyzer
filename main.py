import string

COMMON_PASSWORDS = {
    "password",
    "password123",
    "12345678",
    "qwerty123",
    "admin123",
}

def analyze_password(password):
    suggestions = []
    score = 0

    if not password:
        return "Invalid", ["Enter a password to analyze."]

    if password.lower() in COMMON_PASSWORDS:
        return "Weak", [
            "Avoid common passwords.",
            "Choose a longer, unique password."
        ]

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        suggestions.append("Use at least 12 characters.")
    else:
        suggestions.append("Use a longer password.")

    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Consider lowercase letters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Consider uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Consider numbers.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        suggestions.append("Consider special characters.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


if __name__ == "__main__":
    password = input("Enter a test password: ")
    strength, suggestions = analyze_password(password)

    print("\nPassword strength:", strength)

    if suggestions:
        print("Suggestions:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("No basic improvements suggested.")