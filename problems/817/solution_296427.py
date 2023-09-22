def acima_da_media(lista):
    """retorna as notas que ficaram acima da media"""
    media = sum(lista)/len(lista)
    juncao = lista+[media]
    list.sort(juncao)
    posicao_media = list.index(juncao,media)
    lista_edit = juncao[posicao_media:]
    lista2= list.remove(lista_edit,media)
    return lista_edit