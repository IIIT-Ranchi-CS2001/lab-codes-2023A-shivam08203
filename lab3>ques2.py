n= int(input("Enter a Number: "))

sum_of_digits = 0
x = n

while x > 0:
    digit = x % 10
    sum_of_digits += digit
    x //= 10

print(f" Sum of digits: {sum_of_digits}")