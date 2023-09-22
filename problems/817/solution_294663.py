def insere(lista_numero,n):
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero
def maiores(lista_numero,n):
    ordenada= insere(lista_numero,n)
    return ordenada[list.index(ordenada,n)+1:]
def acima_da_media(notas):
    media= sum(notas)/len(notas)
    return maiores(notas,int(media))