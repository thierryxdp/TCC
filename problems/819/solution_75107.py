def filtraMultiplos(lista,n):
    '''funcao que dado uma lista e um numero n retorna todos os valores da lista multiplos de n 
    list,int->list'''
    x=lista
    y=0
    
    if lista[y]%n==0:
        return lista[y]