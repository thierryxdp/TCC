def maiores(lista,n):
    lista_maiores = list()
    inserir = lista.append(n)
    ordenar = lista.sort()
    i = lista.index(n)
    return lista[i+1:]
def acima_da_media(lista):
    soma = sum(lista)
    tam = len(lista)
    n = soma/tam
    if lista[0]==n:
    	lista.remove(lista[0])
    return maiores(lista,n)