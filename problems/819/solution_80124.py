def filtraMultiplos(listo, n):
    '''Coloque uma lista de números(listo) e um número(n), o resultado será uma lista com os números de 'listo' divisiveis por n
       tuple, int ->list'''
    lista=list(listo)
    lista1=[]
    i=0
    while i<len(lista):
        if lista[i]%n==0:
            lista1.append(lista[i], )
        i=i+1
    return lista1