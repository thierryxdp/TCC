def filtraMultiplos(lista,n):
    '''funcao que dado uma lista e um numero n retorna todos os valores da lista multiplos de n 
    list,int->list'''
    x=lista
    y=0
    while x[y]>=n:
        if x[y]%n==0:
            y=y+1
    return x[y]