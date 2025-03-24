num = int(input("Enter a number: "))
sum_digits = sum(int(digit) ** 3 for digit in str(num))
if num == sum_digits:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")