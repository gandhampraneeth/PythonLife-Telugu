x='''
1=credit
2=debit
3=Exit
'''
user='ajay'
pass_word=5252
user_name=input("Enter the name")
pass_word=input("Enter the password")
if user==user_name and pass_word==pass_word:
    print(x)
    option=int(input("Enter the option:"))
    amount=9
    if option==1:
        credit_amount=float(input("Enter the amount"))
        a=amount+credit_amount
        print("amount after credited",a)
    elif option==2:
        debit_amount=float(input("Enter the amount"))
        a=amount-debit_amount
        print("amount after debited",a)
    elif option==3:
        print("Thanks")
    else:
        print("Enter the correct option")
        
   
        
        

    