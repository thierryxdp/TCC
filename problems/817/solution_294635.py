def maiores(lista,n):
    lista.append(n)
    lista.sort()
    comeco_nova_lista = lista.index(n)
    return lista[comeco_nova_lista+1:]

def acima_da_media(lista):
    media = sum(lista)/len(lista)
    return maiores(lista,media)