# adding the n number of numbers

a = int(input("Enter a number : "))

l=[]

for i in range(0,a+1):
    l.append(i)
    
print(l)
total = sum(l)
print(total)
# difference between first n natural numbers and natural numbers is not including the n 
