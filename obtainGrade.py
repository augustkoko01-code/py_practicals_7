# Obtain Grade Program
# This program determines the grade for each student based on
# their average mark and displays the results in a table.

# Return the grade based on the student's average mark.
def obtain_grade(mark):
    if mark >= 84.5:
        return "A+"
    elif mark >= 79.5:
        return "A"
    elif mark >= 74.5:
        return "B+"
    elif mark >= 69.5:
        return "B"
    elif mark >= 64.5:
        return "C+"
    elif mark >= 59.5:
        return "C"
    elif mark >= 54.5:
        return "D+"
    elif mark >= 49.5:
        return "D"
    else:
        return "F"


# List containing student names and average marks.
mark_list = [
    ['Mary', 90.5],
    ['Charles', 60.4],
    ['John', 70.5],
    ['Javier', 32.0],
    ['Luke', 46.7]
]

# Display the table heading.
print(f"{'Student Name':<15}{'Marks':<15}{'Grade':<15}")

# Process each student in the list.
for student in mark_list:

    # Extract the student's name and mark.
    name = student[0]
    mark = student[1]

    # Determine the student's grade.
    grade = obtain_grade(mark)

    # Display the student's details.
    print(f"{name:<15}{mark:<15}{grade:<15}")