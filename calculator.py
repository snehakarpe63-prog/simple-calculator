a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

ch = int(input("Choice: "))

if ch == 1:
    print("Answer =", a + b)
elif ch == 2:
    print("Answer =", a - b)
elif ch == 3:
    print("Answer =", a * b)
elif ch == 4:
    print("Answer =", a / b)
else:
    print("Invalid Choice")
