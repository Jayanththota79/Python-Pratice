# Numbers that are divisble by 7 and 5

a = int(input("Enter one : "))
b = int(input("Enter another : "))

l=[]

for i in range(a,b):
    if (i%5==0) or (i%7==0):
        l.append(str(i)) 

# code is perfect but we need to print all the numbers in a row   
# created list name called l and stoing all the numbers in list to print in one line 

print(l)
