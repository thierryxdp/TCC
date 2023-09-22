import math
def acima_da_media2(notas):
    """função que recebe uma lista com as notas de uma turma e retorna uma lista ordenada com as notas acima da média"""
    """lista->lista"""
    media=math.ceil(((sum(notas))/(len(notas))))
    list.append(notas, media)
    notas1=sorted(notas)
    return notas1[list.index(notas1,media)+1:]