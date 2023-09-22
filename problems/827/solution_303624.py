import math
def qtd_divisores(v):
    '''retorna a quantidade de divisores do numero de entrada 
    int -> int'''
    b=[]
    for a in range (1, v+1):
        if v%a == 0 :
            b.append(a)
    return len(b)