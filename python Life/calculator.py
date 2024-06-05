# calcualtor
p={1:"add",2:"subtract",3:"multiply",4:"divide"}
option=int(input("Enter 1/add,2/subtract,3/multiply,4/divide"))
if option==1:
   def add():
      a=int(input("Enter the first number:"))
      b=int(input("Enter the second number"))
      return a+b
   print(add())
elif option==2:
   def subtract():
      a=int(input("Enter the first number:"))
      b=int(input("Enter the second number"))
      return a-b
   print(subtract())
elif option==3:
   def multiply():
      a=int(input("Enter the first number:"))
      b=int(input("Enter the second number"))
      return a*b
   print(multiply())
elif option==4:
   def divide():
      a=int(input("Enter the first number:"))
      b=int(input("Enter the second number"))
      return a/b
   print(divide())
   pass
else:
   print("invalid")
   

