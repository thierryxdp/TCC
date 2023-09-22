def filtraMultiplos(lista,n):
    """ Função que recebe uma lista como entrada e numero n e retorna uma lista só com osnúmeros que forem divisíveis por n; list,int-> list"""
    x=range(lista)
    x=x%n
    while x==0:
        return x