print("Hello this file is of git")


#Student Marks Average Caluclation

print("==== Average Caluclator ====")

student_name = str(input("Student Name:"))
student_roll = int(input("Student RollNo:"))

maths = float(input())
Science = float(input())
social = float(input())

total_marks = maths+Science+social
average = total_marks/3

student_list = [85,57,95]
print(student_list)
student_list.append(79)
student_list[3] = 87
avg_list = sum(student_list)/len(student_list)
print(student_list)
print(avg_list)

ele_item = ["TV","washing machine", "refregitator","oven"]
ele_item.append("mobiles")
ele_item.pop(1)
print(ele_item)

print("Average Marks:", average)
print(student_name)

print("Hello to github")

