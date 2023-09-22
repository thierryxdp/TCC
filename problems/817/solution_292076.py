def acima_da_media(notas):
    """Função que calcula a media dos alunos dado suas notas(float) e retorna uma lista contendo as notas acima da
    media. Caso não tenha nenhuma nota acima da média, a função retoma uma lista vazia."""
    media = []
    media1= sum(notas)/len(notas)
    for item in notas:
        if item>media1:
            media.append(item)
    media.sort()
    return media