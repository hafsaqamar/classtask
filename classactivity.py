a=int(input("ENTER VALUE 1: "))

def enofunc(num1):
  if num1%2==0:
      return True
  else:
      return False
result=enofunc(a) 
if result==True:
    print("the value is even")
else: 
    print("the value is odd")