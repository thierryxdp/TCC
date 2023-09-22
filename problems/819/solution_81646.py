def filtraMultiplos(Lista,n):
    """Função que retorna uma lista dos valores divididos por n, de uma lista fornecida"""
    a=0
    lista =[]
    while len(Lista)>a:
        if Lista[a]%n==0:
            lista=lista+[Lista[a]]
        a=a+1
    return lista