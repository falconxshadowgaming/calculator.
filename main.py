def add(p, q):
    return p+q

def subtract(p, q):
    return p-q

def multiply(p, q):
    return p*q

def divide(p, q):
    return p/q

print("Please select the operation: ")
print("A. add B. subtract C. multiply D. divide")
choice=input("Enter your choice A/B/C/D: ")
n1=int(input("Enter the 1st number: "))
n2=int(input("Enter the 2nd number: "))
if choice=="A":
    print("The result is", add (n1, n2))
elif choice=="B":
    print("The result is", subtract (n1, n2))
elif choice=="C":
    print("The result is", multiply (n1, n2))
elif choice=="D":
    print("The result is", divide (n1, n2))
else:
    print("This is an invalid input!")