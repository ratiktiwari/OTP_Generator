import random as r

def otgen():
    ot=""
    for i in range(4):
        ot+=str(r.randint(1,9))
    print ("Your One Time Password is ")
    print (ot)
otgen()
