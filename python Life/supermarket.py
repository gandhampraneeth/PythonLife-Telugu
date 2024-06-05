#super market bill
name=input("Enter your Name:")
from datetime import datetime
lists='''
Rice=       Rs 25/kg
sugar=      Rs 20/kg
oil=        Rs 50/litre
closeup=    Rs 20/1peice
santoor=    Rs 10/each
xxx soap=   Rs 10/eacn
chicken=    Rs 140/kg
'''
#for declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
#rates for items
items={'rice':25,'sugar':20,'oil':50,'closeup':20,'santoor':10,'xxx':10,'chicken':140}
option=int(input("Press 1 for list of items"))
if option==1:
    print(lists)
    for i in range(len(items)):
        inp1=int(input("If you want to buy press 1 or 2 for exit"))
        if inp1==2:
            break
        if inp1==1:
            item=input("Enter your item:")
            quantity=int(input("Enter  quantity:"))
            if item in items.keys():
                price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
           
            finalamount=totalprice
            print(finalamount)
        else:
            print("sorry item unavilable")
    



                 
                 
            
        
           

