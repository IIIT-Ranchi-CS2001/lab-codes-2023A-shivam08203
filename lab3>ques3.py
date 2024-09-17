n = int(input("Enter a positive integer: "))

x, y = 0, 1
sum = 0

while sum < n:
    print(f"{x}")
    z = x + y
    x = y
    y = z
    sum += 1