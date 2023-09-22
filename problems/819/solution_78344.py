def filtraMultiplos(lista,n):
    """ Função que recebe uma lista como entrada e numero n e retorna uma lista só com osnúmeros que forem divisíveis por n; list,int-> list"""
    lista1=lista%n
    n1= range(n)
    while lista1 in n1:
        return lista1