def maiores(lista, n):
    """Funcao retorna uma lista com os elementos da lista original dada:
    lista que sao maiores que o numero dado: n """

    if n in lista:
        lista.sort()
        posicao = lista.index(n)
        lista_final = lista[posicao+1:]
    else:
        lista.append(n)
        lista.sort()
        posicao = lista.index(n)
        lista_final = lista[posicao+1:]

    return lista_final

def acima_da_media(lista_notas):
    """Funcao retorna as notas que ficaram acima da media dada a lista
    com as notas: lista_notas"""

    num_notas = len(lista_notas)
    media = sum(lista_notas)/num_notas
    notas_media = maiores(lista_notas, media)

    return notas_media