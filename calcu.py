def add(a,b):
    result=a+b
    print(result)
def sub(a,b):
    result=a-b
    print(result)

choose=input("choose any one operator +,-")
firstnum=int(input("enter 1 number"))
secondnum=int(input("enter 2 number"))


if choose=='+':
    add(firstnum,secondnum)
if choose=='-':
    sub(firstnum,secondnum)