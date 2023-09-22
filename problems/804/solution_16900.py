def filtra_pares(a,b,c,d):
    '''função que retorna a partir de uma tupla com quatro elementos inteiros, uma outra tupla contendo apenas os pares da tupla original. [entradas -> int,int,int,int] [saida -> int:]'''
    if a%2==0:
        return a
    if a%2==0 and b%2==0 and c%2==0 and d%2==0:
        return a,b,c,d
    if a%2==0 and b%2==0:
        return a,b