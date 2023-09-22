def filtraMultiplos(lista,n):
    '''funcao que dado uma lista e um numero n retorna todos os valores da lista multiplos de n 
    list,int->list'''
    x=lista
    y=0
    while y>=n:
        if lista[y]==0:
            return lista[y]
        y+=1