def maiorN(valor,n):
    return valor<n
def maiores(lista,n):
    lista= list(filter(maiorN, lista))
    return lista