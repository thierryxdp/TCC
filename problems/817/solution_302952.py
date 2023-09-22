def maiores (lista,n):
    nova_lista = []
    for e in lista:
        if e > n:
            list.append(nova_lista,e)
            list.sort(nova_lista)
    return nova_lista

def acima_da_media(lista):
    for e in lista:
        a = sum(lista) / len(lista)
    return maiores(lista,a)