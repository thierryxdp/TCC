def filtraMultiplos(lista,n):
    '''
    dada uma lista e um numero n retorna uma nova lista
    com os numeros da lista multiplos por n
    entrada:lista,int
    saida:lista
    '''
    
    Multiplos=[]
    i=0
    while i <len(lista):
        if lista[i]%n == 0:
            list.append(Multiplos,lista[i])
        i=i+1
    return Multiplos