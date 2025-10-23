python_students={"Fathima","Nivedya","Jeena"}
ds_students={"Anjana","Ryan","Fathima"}

python_students.add("Nandana")

ds_students.remove("Ryan")

both_courses= python_students.intersection(ds_students)
print("Students in both courses:", both_courses)

only_python = python_students - ds_students
print("Students only in Python:", only_python)

all_students = python_students.union(ds_students)
print("All students in either course:", all_students)

course_dict ={
    "Python": len(python_students),
    "Data science" : len(ds_students)
}
print ("Dictionary with course names:",course_dict)

for course,count in course_dict.items():
     print("Course:", course, ", Students:", count)

growth_dict = {course: count * 2 for course, count in course_dict.items()}
print("Expected growth in students:", growth_dict)