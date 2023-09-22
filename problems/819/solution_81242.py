def filtraMultiplos(lista,n):
    '''
    retorna quais numeros da lista sao multiplos
    list -> n
    '''
    lista_multi=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            lista_multi.append(lista[i])
            i=i+1
    return lista_multi