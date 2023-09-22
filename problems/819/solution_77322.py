def filtraMutiplos(lista,n):
    '''ok'''
    lista2=[termo for termo in lista if termo %n==0]
    return lista2