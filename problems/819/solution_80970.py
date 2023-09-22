def filtraMultiplos(lista, n):
    '''funcao que, dada uma lista de números e um número n, retorna uma nova lista com os
    multiplos de n;
    list(int),int->list(int)'''
    multiplos=[]
    indice=0
    while indice<len(lista):
        if lista[indice]%n==0:
            multiplos = multiplos + [lista[indice],]
        indice = indice + 1
    return multiplos