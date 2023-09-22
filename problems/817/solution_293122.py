if n not in lista:
lista = lista+[n]
def acima_da_media(lista1):
	media=sum(lista1)/len(lista1)
    return maiores(lista1,media)
def maiores(lista,n):
    lista.append(n)
    lista.sort()
    indice=lista.index(n)
    return lista[indice+1:]