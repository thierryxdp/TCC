def acima_da_media(notas):
    '''função que recebe uma lista com as notas dos alunos
    de uma turma e retorna uma lista com as notas acima da
    média
    list -> list'''
    media = sum(notas) / len(notas)
    list.sort(notas)
    a = 0
    notas_acima = []
    while a < len(notas):
        if notas[a] > media:
            list.append(notas_acima,notas[a])
    return notas_acima