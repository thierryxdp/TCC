def acima_da_media(lista):
    """Dada uma lista com as notas dos alunos, retorna uma lista ordenada
    com as notas que ficaram acima da média"""
    media = sum(lista)/len(lista)
    list.append(lista,media)
    ordenada = sorted(lista)
    indice = list.index(ordenada,media)
    lista_acima = ordenada[indice+1:]

    return lista_acima