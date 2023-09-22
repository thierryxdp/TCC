"""Recebe uma lista com as notas dos alunos de uma turma e retorna uma
nova lista ordenada com as notas que estão acima da média da turma
list-> list"""

def acima_da_media(notas_alunos):
    media = sum(notas_alunos)/len(notas_alunos)
    notas_acima_media = []
    for i in range (len(notas_alunos)):
        if notas_alunos[i] >= media:
            notas_acima_media.append(notas_alunos[i])
    notas_acima_media.sort()
    return notas_acima_media