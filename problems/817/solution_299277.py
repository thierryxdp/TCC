def acima_da_media(notas):
    """função que recebe uma lista com as notas de uma turma e retorna uma lista ordenada com as notas acima da média"""
    """lista->lista"""
    media=int(((sum(notas))/(len(notas))))
    list.append(notas, media)
    notas1=sorted(notas)
    x=list.index(notas,media)
    return notas1[list.index(notas1,media)+1:]