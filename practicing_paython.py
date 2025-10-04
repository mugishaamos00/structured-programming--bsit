
# Part a
def get_best_two_average(t1, t2, t3):
    
    tests = [t1, t2, t3]

    tests.remove(min(tests))

    return sum(tests) / 2

def get_grade(total):
    if total >= 80:
        return "A"
    elif total >= 75:
        return "B+"
    elif total >= 70:
        return "B"
    elif total >= 65:
        return "B-"
    elif total >= 60:
        return "C+"
    elif total >= 55:
        return "C"
    elif total >= 50:
        return "D"
    else:
        return "F"

test1 = float(input("Enter marks for Test 1: "))
test2 = float(input("Enter marks for Test 2: "))
test3 = float(input("Enter marks for Test 3: "))
exam = float(input("Enter marks for Exam: "))

avg_tests = get_best_two_average(test1, test2, test3)
total = avg_tests + exam
print(f"Total marks (best two tests average + exam): {total}")

choice = input("Type 'grade' to see your letter grade or 'end' to exit: ").strip().lower()
if choice == "grade":
    print(f"Your grade is: {get_grade(total)}")
else:
    print("Goodbye!")             


# Part b
year = input("Enter year (YYYY): ")
month = input("Enter month (MM): ")
course = input("Enter course code: ")
import random
unique = str(random.randint(1000, 9999))
vu_id = f"VU{year}{month}{course.upper()}{unique}"
print(f"Your VU ID number is: {vu_id}")


# Part c
import os
paragraph = input("Enter a paragraph: ")
documents_folder = os.path.join(os.path.expanduser("~"), "Documents")
os.makedirs(documents_folder, exist_ok=True)
file_path = os.path.join(documents_folder, "doc.txt")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(paragraph)

print(f"Paragraph saved to {file_path}")