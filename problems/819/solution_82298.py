def filtraMultiplos(lista,n):
    """
    recebe uma lista e um número e retorna uma sublista com os elementos
    da original que são divisíveis por 'n'
    """
    i=0
    lista2=[]
    
    while i<len(lista):
        if lista[i]%n==0:
            list.append(lista2,lista[i])
        i=i+1
    return lista2