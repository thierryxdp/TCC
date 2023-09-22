def filtraMultiplos(lista,n):
    '''Retorna uma lista com numeros multiplos de n
    list,int->list'''
    multiplos=[]
    i=0
    while i<len(lista):
        if lista[i] % n == 0:
            multiplos.append(lista[i])
        i=i+1
    return multiplos