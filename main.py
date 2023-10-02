# 1.1 Echo String
echo = input("Enter some text: Hello, World! ECHO!  ")
print = input("Hello, World! ECHO!")

# 1.2 Adding a number to an integer
num = input("Enter a number: ")
new_num = int(num) + 1
print(new_num)

# 1.3 Adding a number to a float
num = input("Enter a number: ")
new_num = int(num) + 0.5
print(new_num)

# # 1.4 Adding Two Floats
num = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
total = num + num2
print(f"The sum is {total} ")

# # 1.5 Multiplying Floats
num = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
total = num * num2
print(f"The product is {total}")


# 1.6 Dividing Integers
num = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
total = num / num2
print(f"The result is {total}")

# 1.7 Entering booleans
prompt = input("Enter a boolean: ")
print(f"You entered: {prompt}")
if prompt == "True":
    print("The opposite of what you entered is: False")
elif prompt == "False":
    print("The opposite of what you entered is: True")




