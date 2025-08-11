# calculator 

a = int(input("Enter a number : "))

b = int(input("enter aother number"))

operation = input(" Enter operation (+, -, %, /) : ")

result = None 

# we created a result with none value to store the number after the operation 
# wriring the if loop 

if operation == "+":
    result = a+b
    print(result)

elif operation == "-":
    result = a-b
    print(result)
elif operation == "%":  # % operator will print the reminder
    result = a%b
    print(result)
elif operation == "/": 
    result = a/b
    print(result)

# caluclator having only addition subraction divison
