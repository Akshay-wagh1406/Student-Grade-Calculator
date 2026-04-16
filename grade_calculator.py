# 🎯 Student Grade Calculator

def calculate_grade(marks):
    """Function to calculate grade and message based on marks"""
    if marks >= 90:
        return "A", "Excellent! You're a star! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good job! You can do even better! 😊"
    elif marks >= 60:
        return "D", "Nice effort! Keep practicing! 💪"
    else:
        return "F", "Don't give up! Try again! 🚀"


# Get student name
name = input("Enter student name: ")

# Input validation using while loop
while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("❌ Please enter marks between 0 and 100.")
    except ValueError:
        print("❌ Invalid input! Please enter a number.")

# Calculate grade
grade, message = calculate_grade(marks)

# Display result
print("\n📊 RESULT FOR", name.upper() + ":")
print("Marks:", marks, "/100")
print("Grade:", grade)
print("Message:", message)