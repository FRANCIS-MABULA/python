marks = [70, 82, 38, 99, 42, 38, 67]
passes = 0
fails = 0
total_marks = 0
num_of_marks = 0

for mark in marks:
    total_marks += mark
    num_of_marks += 1
    if mark >= 50:
        passes += 1
    else:
        fails += 1
average_mark = int(total_marks / num_of_marks)
highest_mark = max(marks)
lowest_mark = min(marks)

print("Number of students who passes: ", passes)
print("Number of students who failed: ", fails)
print("Total Marks: ", total_marks)
print("Average Mark ", average_mark)
print("The highest mark is: ", highest_mark)
print("The lowest mark is: ", lowest_mark)
