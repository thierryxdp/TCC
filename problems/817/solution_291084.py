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

def acima_da_nota(lista_notas):
    """Funcao retorna a media da turma dada a lista com as notas: lista_notas
    e tambem retorna uma lista com as notas que ficaram acima da media """

    num_notas = len(lista_notas)
    media = sum(lista_notas)/num_notas
    notas_media = maiores(lista_notas, media)

    return media, notas_media