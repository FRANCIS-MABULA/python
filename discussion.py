results = int(input("Enter result: "))
if results >=80:
    grade = "A"
elif results >=70:
    grade = "B"
elif results >=50:
    grade = "C"
else:
    grade = "D"
    print(f"Grade: {grade}")