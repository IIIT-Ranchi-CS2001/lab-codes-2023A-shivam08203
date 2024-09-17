strinput = input("Enter a string: ")

for char in strinput:
    if not char.isalnum():
        print(False)
        break
else:
    print(True)