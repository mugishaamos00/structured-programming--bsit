'''
Arithmetic Operators:
Used for calculations such as addition (+), division (/), and finding the minimum (min() uses comparison internally).
Example: Calculating the average of the best two tests and the total marks.

Assignment Operators:
Used to assign values to variables, e.g., =.
Example: total = avg_tests + exam

Comparison Operators:
Used to compare values, e.g., >=, <=.
Example: Determining the grade based on the total marks.

Logical Operators:
Used in conditional statements to combine multiple conditions, e.g., and, or.

String Operators:
Used for concatenation, e.g., + to build the VU ID.

Input/Output Operators:
input() and print() are used for user interaction.

'''

# Part b
student_ids = ["VU202309CS1001", "VU202308IT1002", "VU202310CS1003", "VU202307EE1004"]
student_ids.sort(reverse=True)
print("Student IDs in descending order:")
for sid in student_ids:
    print(sid)

# Part c
import os

documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
file_path = os.path.join(documents_folder, "doc.txt")

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

half_length = len(content) // 2
reduced_content = content[:half_length]

print("Reduced content:")
print(reduced_content)