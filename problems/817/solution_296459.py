def maiores(lista_numero, n):
    listan = [n,]
    nova_lista = lista_numero + listan
    list.sort(nova_lista)
    ind_n = list.index(nova_lista,n)
    nova_lista1 = nova_lista[ind_n+1:]
    return nova_lista1

def acima_da_media(notas):
    if len(notas) = 1:
        return []
    elif:
        media = sum(notas)/len(notas)
        nova_lista = maiores(notas,media)
        return nova_lista