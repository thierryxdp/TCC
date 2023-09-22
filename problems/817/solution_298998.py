import math.ceil
def acima_da_media(notas):
    '''crie uma funcao que, dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da média. list-->list.'''
    media = math.ceil((sum(notas))/(len(notas)))
    if len(notas) <= 1:
        return []
    elif media in notas:
        list.sort(notas)
        index = list.index(notas, media)
        return notas[index + 1:]
    else:
        list.append(notas,media)
        list.sort(notas)
        notas_altas = list.index(notas,media)
        return notas[notas_altas + 1:]