# Student Grade Calculator

num_subjects = int(input("Enter the number of subjects: "))

total_marks = 0

# Input marks for each subject
for i in range(1, num_subjects + 1):
    marks = int(input(f"Enter marks for subject {i} (out of 100): "))
    total_marks += marks

# Calculate average percentage
average_percentage = total_marks / num_subjects

# Grade calculation
if average_percentage >= 90:
    grade = 'A'
elif average_percentage >= 80:
    grade = 'B'
elif average_percentage >= 70:
    grade = 'C'
elif average_percentage >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display results
print("\nResults")
print("Total Marks:", total_marks)
print("Average Percentage:", average_percentage, "%")
print("Grade:", grade)
