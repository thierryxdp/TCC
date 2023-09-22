def acima_da_media(lista):
    '''dada uma lista com as notas dos alunos de uma turma, retorna as notas que estao acima da media; list-> list'''
    Q = len(lista)
    S = sum(lista)
    media = S/Q
    acima = maiores(lista,media)
    return acima