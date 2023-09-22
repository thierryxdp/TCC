def filtraMultiplos(lista,n):
    '''função que recebe uma lista de números e retorna outra lista com os números divisiveis por n; list, int => list'''
    lista1=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            lista1=lista1+[lista[i]]
        i=i+1
    return lista1