a=10

#def hello():
    #a=22
    #print(a)

#print(a)
#hello()

def outer():
    a=8
    def inner():
        a=23
        print('inner sees a as',a)

    print('outer sees as',a)

outer()