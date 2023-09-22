def filtraMultiplos(lista,n):
    '''função que a partir de uma lista com números inteiros e um inteiro 'n' devolve uma lista contendo quais números dessa lista inicial são múltiplos desse número n;list,int->list'''
    i=0
    multiplos=[]
    while i<len(lista):
        if lista[i]%n==0:
            multiplos = multiplos + [lista[i],]
        i=i+1
    return multiplos