marks = [70, 80, 90, 50, 40, 30]
passed = 0
failed = 0
for mark in marks:
    if mark >=50:
        passed = passed + 1
        print(passed)
    else:
        failed = failed + 1
        print(failed)