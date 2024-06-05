#used to read,write,rename,close
'''
r=read
w=write

'''


# file=open("demo.txt",mode="r")
# p=file.readlines()
# print(p)
# file.close()



file=open("demo.txt",mode="a")
p=file.write("i love you to") # data loss when we use write
#no data loss by append

file.close()
