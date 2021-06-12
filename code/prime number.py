a=int(input("enter a number = "))
fact=[]
for i in range(1,a+1):
    if a%i==0:
       fact.append(i)
print ("Factors of {} = {}".format(a,fact))
if len(fact)<=4 :
    print("It is near prime number")
else:
    print("It is not near prime number")
