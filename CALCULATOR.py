
def add(firstnum, secondnum):
   return firstnum + secondnum

def subtract(firstnum, secondnum):
   return firstnum - secondnum

def multiply(firstnum, secondnum):
   return firstnum * secondnum

def divide(firstnum, secondnum):
   return firstnum / secondnum

print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")


operations = input("Enter Operation:")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if operations == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif operations == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif operations == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif operations == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")
