def filtraMultiplos(lista,n):
    ''' Filtra quais numeros da lista são múltiplos de um numero n e
    retorna uma nova lista com apenas os múltiplos;
    list,int -> list'''
    i=0
    multiplos=[]
    while i<len(lista):
        if lista[i]%n==0:
            list.append(multiplos,lista[i])
        i=i+1
    return multiplos