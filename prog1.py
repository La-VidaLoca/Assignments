print("Quadratic Equation: ax^2 + bx + c = 0")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    root1 = (-b + discriminant ** 0.5) / (2 * a)
    root2 = (-b - discriminant ** 0.5) / (2 * a)
    print("The roots of the equation are:", root1, root2)
elif discriminant == 0:
    root = -b / (2 * a)
    print("The roots of the equation are:", root)
else:
    real_part = -b / (2 * a)
    imaginary_part = (-discriminant) ** 0.5 / (2 * a)
    print("The roots of the equation are:", real_part + imaginary_part * 1j, real_part - imaginary_part * 1j)