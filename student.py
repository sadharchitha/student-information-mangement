name = input("Enter student name: ")
age = int(input("Enter student age: "))
grade = float(input("Enter student grade: "))
if age >= 18:
    print("Student is eligible for admission!")
elif age >= 16:
    print("Student is eligible for conditional admission!")
else:
    print("Student is not eligible for admission!")
if grade >= 80:
    print("Student has good grades!")
elif grade >= 60:
    print("Student has average grades!")
else:
    print("Student has poor grades!")
if grade >= 90 and age >= 18:
    print("Student is eligible for scholarship!")
elif grade >= 80 and age >= 18:
    print("Student is eligible for partial scholarship!")
else:
    print("Student is not eligible for scholarship!")
if age >= 16 and grade >= 70:
    print("Student is eligible for extracurricular activities!")
elif age >= 14 and grade >= 60:
    print("Student is eligible for partial extracurricular activities!")
else:
    print("Student is not eligible for extracurricular activities!")
classes_attended = int(input("Enter number of classes attended: "))
if classes_attended >= 90:
    print("Student has attended all classes!")
elif classes_attended >= 80:
    print("Student has attended most classes!")
else:
    print("Student has not attended all classes!")
assignments_submitted = int(input("Enter number of assignments submitted: "))
if assignments_submitted >= 10:
    print("Student has submitted all assignments!")
elif assignments_submitted >= 8:
    print("Student has submitted most assignments!")
else:
    print("Student has not submitted all assignments!")
if grade >= 80 and classes_attended >= 90 and assignments_submitted >= 10:
    print("Student is eligible for graduation!")
elif grade >= 70 and classes_attended >= 80 and assignments_submitted >= 8:
    print("Student is eligible for conditional graduation!")
else:
    print("Student is not eligible for graduation!")
outstanding_fees = float(input("Enter outstanding fees: "))
if outstanding_fees > 0:
    print("Student has outstanding fees!")
else:
    print("Student does not have outstanding fees!")
if grade >= 80 and age >= 18 and outstanding_fees == 0:
    print("Student is eligible for alumni membership!")
elif grade >= 70 and age >= 18 and outstanding_fees == 0:
    print("Student is eligible for conditional alumni membership!")
else:
    print("Student is not eligible for alumni membership")
special_needs = input("Enter special needs (yes/no): ")
if special_needs.lower() == "yes":
    print("Student has special needs!")
else:
    print("Student does not have special needs!")
if special_needs.lower() == "yes" and age >= 18:
    print("Student is eligible for disability services!")
elif special_needs.lower() == "yes" and age >= 16:
    print("Student is eligible for conditional disability services!")
else:
    print("Student is not eligible for disability services!")
medical_conditions = input("Enter medical conditions (yes/no): ")
if medical_conditions.lower() == "yes":
    print("Student has medical conditions!")
else:
    print("Student does not have medical conditions!")
if medical_conditions.lower() == "yes" and age >= 18:
    print("Student is eligible for medical services!")
elif medical_conditions.lower() == "yes" and age >= 16:
    print("Student is eligible for conditional medical services!")
else:
    print("Student is not eligible for medical services!")