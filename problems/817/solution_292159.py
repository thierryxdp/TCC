def acima_da_media(notas):
    """Esta função recebe uma lista com as notas dos alunos e devolve uma outra lista com as notas que estão acima da média da turma em ordem crescente
    list -> list"""
    soma_das_notas = 0
    acima_da_media = []
    for nota in notas:
        soma_das_notas += nota
    for i in notas:
        if i > soma_das_notas:
            acima_da_media.append(i)
            acima_da_media.sort()
    return acima_da_media