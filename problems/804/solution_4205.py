def par(num):
    return num%2==0

def filtra_pares(e1,e2,e3,e4):
    ""
    elemento1==par(e1)
    elemento2==par(e2)
    elemento3==par(e3)
    elemento4==par(e4)
    if elemento1==True and elemento2==True and elemento3==True and elemento4==True:
        return elemento1, elemento2, elemento3, elemento4
    else:
        if elemento1==True and elemento2==True elemento3==True and elemento4==False:
            return elemento1,elemeto2,elemento3