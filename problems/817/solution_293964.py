def acima_da_media(lista):
    """Função que, dado uma lista, retorna a media das notas do aluno, junto a lista ordenada das notas acima da media.
    lista - > float, lista"""
    media_notas = sum(lista)/len(lista)
    return (media_notas, maiores(lista,media_notas))