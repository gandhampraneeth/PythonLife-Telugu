#looping or iterative statements
#if we want to excute statements multiple times then we use looping statements.
# two types for loop & while looop

# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end=" ")
# print()
#while loop
# prani=7
# while prani<10:
#     print("this is while",prani)
#     prani+=1



# user="prani"
# pass_word="prani123"
# user_name=input("Enter the username")
# pass_word=input("Enter the password")
# if user==user_name and pass_word==pass_word:
#     print("success")
# else:
#     print("invalid")

'''

'WHILE LOOP= a statement that excutes its a block of code as long as its condition remains true'

# name=''
# while len(name)==0:
#     name=input('enter your name')
# print('hi hello' +  name)

'FOR LOOP= a statement that excutes its a block of code for limited time'
'''
# while loop= unlimited
# for loop= limited
'''
# for i in range(10):
#     print(i+1)
# for i in range(20,50+1):
#     print(i)
# name='praneeth'
# for i in name:
#         print(i)
'''

n=int(input('Enter the number'))
for i in range(n):
    for j in range(i+1):
        print('*',end='  ')
    print()



'''
LOOP control statements= used to change a excution from its normal sequence
break= used to terminate entire loop
continue= skip to the next iteration of loop
pass= acts as place holder
'''
# while True:
#     number=input("enter the number")
#     if number!='':
#         break
# phone_number = '9542-505-714'
# for i in phone_number:
#     if i== "-":
#         continue
#     print(i ,end='')

for i in range(0,11):
    if i == 4:
        pass
    else:
         print(i)
