def acima_da_media(lista):
    """Função que recebe uma lista de notas e retorna uma sublista contendo apenas
    as notas maiores que a média das notas recebidas
    list -> list"""
    media = sum(lista)/len(lista)
    list.append(lista, media)
    list.sort(lista)
    posicao_media = list.index(lista, media)
    return lista[posicao_media+1:]