def filtraMultiplos(lista,n):
    '''
    funcao retorna lista com os numeros da lista de entrada divisíveis por n
    '''
    i=0
    h=[]
    while i<len(lista):
        if lista[i]%n==0:
            h.append(lista[i])
        i=i+1
    return h