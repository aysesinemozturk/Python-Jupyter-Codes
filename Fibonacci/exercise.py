terms = int(input("How many terms: "))

num1, num2 = 0,1
count = 0

print("Fibonacci sequence: ")
while count < terms:
    print(num1)
    n = num1 + num2
    num1 = num2
    num2 = n
    count += 1

print(num1)
print(count)
