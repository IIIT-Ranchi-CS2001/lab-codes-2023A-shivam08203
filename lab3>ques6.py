strinput = input("Enter a string: ")
charinput = input("Enter a character: ")
cnt = 0

for char in strinput:
    if char == charinput:
        cnt += 1

print(f"The character '{charinput}' occurs {cnt} times in the string.")