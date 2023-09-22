def maiores(lista,n):
    lista_maiores = list()
    inserir = lista.append(n)
    ordenar = lista.sort()
    i = lista.index(n+1)
    return lista[i+1:]
def acima_da_media(lista):
    soma = sum(lista)
    tam = len(lista)
    n = soma/tam
    return maiores(lista,n)