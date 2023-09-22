def acima_da_media(lista):
    """funcao que recebe uma lista com as notas dos alunos e retorna uma nova lista ordenada apenas com as notas que ficaram acima da media.
    list -> list"""
    media = (sum(lista)//len(lista))+0.1
    lista.append(media)
    lista.sort()
    lista = lista[lista.index(media)+1:]
    return lista