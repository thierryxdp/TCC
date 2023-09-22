def filtraMultiplos(lista,n):
    """ Função que recebe uma lista como entrada e numero n e retorna uma lista só com osnúmeros que forem divisíveis por n; list,int-> list"""
    x=0
    lista1=[]
    while x<len(lista):
        i=lista[x]
        if x%n==0:
            lista1=lista1+[i]
        x=x+1
    return lista1