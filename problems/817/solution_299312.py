def acima_da_media(notas):
    """função que recebe uma lista com as notas de uma turma e retorna uma lista ordenada com as notas acima da média"""
    """lista->lista"""
    media=(sum(notas))/(len(notas))
    list.append(notas, media)
    notas1=sorted(notas)
    x=list.index(notas1,media)
    return notas1[(x+1):]