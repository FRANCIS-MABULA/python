"""
data = [
    ["Francis", "202600142", "Cyber Security"],
    ["Isaac", 20260189, "Computer Science",],
    ["Jonathan ", 202603152, "Computer Science"]
    ]
print(data[0][1])

print(type(data[0][1]))

print(type(data[1][1]))

print(data)

student = ("Student", "Student Number", "Programme!")
student, number, programme = student
print(programme)

"""
#SETS
course_codes = {"ICT111", "ICT101", "ICT131"}
print("ICT111" not in course_codes)

#Dictionaries: Stores data as keys and values
dic = {
    "Student_no": 202602537,
    "name": "Mary"
}
print(dic["name"])
print(dic.keys())
print(dic.values())
print(dic.items())

if "name" in dic:
    print("Present")
else:
    print("Not Present")

#Updatin a dictionary
dic["Programme"] = "Computer Science"

print(dic.items())

dic["Mark"] = "80%"
print(dic)

removed_mark = dic.pop("Mark")
print(removed_mark)

grades = ["A","B","C","A","A","C","B"]
counts = {}
for grade in grades:
    counts[grade] = 