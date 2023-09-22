def filtraMultiplos(lista,n):
    """Dado uma lista de números e um número n, retorna uma lista com os números
    divisíveis por n:
    list,int-->list"""
    numeros=len(lista)
    lista_filtrada=[]
    i=0
    while i<numeros:
        if (lista[i]%n)==0:
            lista_filtrada=lista_filtrada+[lista[i]]
        i+=1
    return lista_filtrada