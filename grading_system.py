use = list(input("Enter something: "))
if use:
    print("You cannot send a blank response.")

print(type(use))
print(use is False)