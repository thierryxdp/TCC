from random import randint

def faltante(L):
    ''' dddede '''
    taman = len(L)+ 1
    x = randint(1,taman)
    
    while x in L:
        if x not in L:
            return x