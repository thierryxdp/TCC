def filtraMultiplos(lista,n):
    '''funcao que dado uma lista e um numero n retorna todos os valores da lista multiplos de n 
    list,int->list'''
    mult=[]
    x=0
    while x<n:
        if lista[x]%n==0:
            mult=mult+lista[x]
        x=x+1
    return mult