i=0
t1=0
t2=1
n=int(input("enter a number:"))
for i in range (0,n):
    print(t1)
    temp=t1+t2
    t1=t2
    t2=temp
    i=i+1
