def acima_da_media(notas):

    ''' lista > lista
    Dada uma lista com as notas dos alunos de uma turma, retorna aquelas que ficaram acima da média'''

    notatotal = sum(notas)
    alunos = len(notas)
    media = notatotal/alunos

    return maiores(notas, media)