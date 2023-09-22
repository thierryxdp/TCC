from random import randint

def faltante(L):
    ''' dddede '''
    taman = len(L)+ 1
    x = randint(0,taman)
    
    while x in L:
        x = randint(1,taman)
        if x not in L:
            return x