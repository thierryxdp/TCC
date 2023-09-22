def insere(lista_numero,n):
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista_numero,n):
    insere(lista_numero,n)
    a=lista_numero[list.index(lista_numero,n)+1:]
    return a

def acima_da_media(lista):
    a=maiores(lista,6)
    return a