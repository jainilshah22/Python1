a=input("Enter number= ")
def determineNo(number):
   upNumber=False
   downNumber=False
   upDownNumber=False
   digit=[int(x) for x in str(a)]
   for i in range(0,len(digit)-1):
       if(digit[i]<=digit[i+1]):
           upNumber=True
       else:
           upNumber=False
           break
   for j in range(0,len(digit)-1):
       if(digit[j]>=digit[j+1]):
           downNumber=True
       else:
           downNumber=False
           break
   for k in range(0,len(digit)-1):
       if(digit[k]<=digit[k+1]):
           upDownNumber=True
       else:
           upDownNumber=False
           break
   for k in range(k,len(digit)-1):
       if(digit[k]>=digit[k+1]):
           upDownNumber=True
       else:
           upDownNumber=False
           break
   if(upNumber==True):
       return "YES"
   elif(downNumber==True):
       return "YES"
   elif(upDownNumber==True):
       return "YES"
   else:
       return "NO"
result=determineNo(a)
if(result=="YES"):
   print("it is a nice number",result)
else:
   print("It is not a nice number NO")
