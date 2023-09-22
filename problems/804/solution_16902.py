def filtra_pares(a,b,c,d):
    '''função que retorna a partir de uma tupla com quatro elementos inteiros, uma outra tupla contendo apenas os pares da tupla original. [entradas -> int,int,int,int] [saida -> int:]'''
    if a,b,c,d = a%2==0,b%2==0,c%2==0,d%2==0:
        return a,b,c,d
    if a,b,c = a%2==0,b%2==0,c%2==0:
        return a,b,c
    a,b = a%2==0,b%2==0:
        return a,b
    if a = a%2==0:
        return a