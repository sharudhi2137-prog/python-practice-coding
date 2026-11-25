a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping:")
print("A =", a)
print("B =", b)

a, b = b, a

print("After swapping:")
print("A =", a)
print("B =", b)

Output
Before swapping:
A = 10
B = 20
After swapping:
A = 20
B = 10
