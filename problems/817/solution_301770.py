def acima_da_media (lista):
    '''dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acimada média;
    list -> list'''
    media=(sum(lista))/(len(lista))
    return maiores(lista,media)