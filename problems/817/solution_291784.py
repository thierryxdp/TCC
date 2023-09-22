def acima_da_media(notas):
    """
    Indica as notas que ficaram acima da media
    Parametros:
    	notas -> list
        notas dos alunos
    Returns:
    	list
        notas acima da média
    """
    media=sum(notas)/len(notas)
    list.append(notas,media)
    list.sort(notas)
    acima_media=notas[notas.index(media)+1:]
    return acima_media