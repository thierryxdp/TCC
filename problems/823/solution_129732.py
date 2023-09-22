from random import randint
def faltante(L):
    '''retorna o numero inteiro que pertence ao intervalo de N elementos mas nao pertence a lista de entrada
    tupla -> int'''
    list.sort(L)
    b=len(L)+1
    a=randint(1,b)
    
    while a in list(range(1,b+1)):
        a=randint(1,b+1)
    return a