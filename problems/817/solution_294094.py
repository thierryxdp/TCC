def acima_da_media(lista):
    """Função que, dado uma lista, retorna a media das notas do aluno, junto a lista ordenada das notas acima da media.
    lista - > float, lista"""
    media_notas = sum(lista)/len(lista) + 0.0001
    list.append(lista, media_notas)
    list.sort(lista)
    posicao= list.index(lista,media_notas)+1
    return (lista[posicao:])