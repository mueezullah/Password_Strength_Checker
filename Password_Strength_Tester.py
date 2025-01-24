# Library: working with regular expressions(e.g, !, @, #)
import re

# Function to check the strength of password
def check_password_strength(password):

    #
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    is_long = len(password) >= 8

    #Calculate the strength of password by summing
    strength_score = sum([has_upper, has_lower, has_digit, has_special, is_long])

    #Provide feedback on how to improve password strength
    feedback = []
    if not has_upper:
        feedback.append("Add at least one uppercase letter")
    if not has_lower:
        feedback.append("Add at least one lowercase letter")
    if not has_digit:
        feedback.append("Add at least one digit")
    if not has_special:
        feedback.append("Add at least one special character(e.g, @, #, $)")
    if not is_long:
        feedback.append("Password must be at least 8 characters long")

    #Password rating based on strength score
    if strength_score == 5:
        rating = "Strong"
    elif 3 <= strength_score < 5:
        rating = "Moderate"
    else:
        rating = "Weak"

    return rating, feedback

def main():
    password = input("Enter the password: ")
    rating, feedback = check_password_strength(password)

    #Display password rating
    print(f"\nPassword rating: {rating}")
    #If there is feedback then display it to improve password
    if feedback:
        print("To improve password, you should: ")
        for suggestion in feedback:
            print(f"- {suggestion}")

#main() function to run script
if __name__ == "__main__":
    main()