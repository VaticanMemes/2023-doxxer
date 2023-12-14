import csv

"""
with open("new_2023_honour_roll.csv", mode="w") as new_hr:
    with open("2023_honour_roll.csv") as hr:
        hr_reader = csv.reader(hr, delimiter=",")
        hr_writer = csv.writer(new_hr, delimiter=',')
        previous_first_name = ""
        previous_last_name = ""
        previous_school = ""
        subjects = []
        for row in hr_reader:
            if row == []:
                continue
            elif row[0] == previous_first_name:
                subjects.append(row[3])
                previous_first_name = row[0]
                previous_last_name = row[1]
                previous_school = row[2]
            elif row[0] != previous_first_name:
                hr_writer.writerow([previous_first_name, previous_last_name, previous_school, " | ".join(subjects)])
                subjects = []
                subjects.append(row[3])
                previous_first_name = row[0]
                previous_last_name = row[1]
                previous_school = row[2]
"""
list_of_students = []
dict_of_student = {}

with open("2023_honour_roll.csv") as hr:
    hr_reader = csv.reader(hr, delimiter=",")
    # hr_writer = csv.writer(new_hr, delimiter=',')
    previous_first_name = "first_name"
    previous_last_name = "last_name"
    previous_school = "school"
    subjects = ["subjects"]
    dict_of_student = {}
    line_count = 0
    for row in hr_reader:
        # print(row)
        if row == []:
            continue
        elif row[0] == previous_first_name:
            subjects.append(row[3])
            previous_first_name = row[0]
            previous_last_name = row[1]
            previous_school = row[2]
        else:
            dict_of_student["First name"] = previous_first_name
            dict_of_student["Last name"] = previous_last_name
            dict_of_student["School"] = previous_school
            dict_of_student["Subjects"] = " | ".join(subjects)
            # print(dict_of_student)
            list_of_students.append(dict_of_student)
            dict_of_student = {}
            subjects = []
            subjects.append(row[3])
            previous_first_name = row[0]
            previous_last_name = row[1]
            previous_school = row[2]

# Plz don't look at the code lol - straight up removing bits of dictionary and adding other bits
del list_of_students[0]
del list_of_students[0]
list_of_students.append({"First name": "Sophia", "Last name": "Zybenko", "School": "Ravenswood School for Girls", "Subjects": "15140 - English Advanced | 15160 - English Extension 1 | 15170 - English Extension 2"})

# For testing: print(list_of_students)

with open("new_2023_honour_roll.csv", mode="w") as new_hr:
    hr_writer = csv.DictWriter(new_hr, fieldnames=["First name", "Last name", "School", "Subjects"], lineterminator='\n', delimiter=',')
    hr_writer.writeheader()
    for item in list_of_students:
        hr_writer.writerow(item)