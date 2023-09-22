def acima_da_media (lista):
    '''Função em que, dada uma lista com as notas dos alunos de uma turma,
    retorne uma lista ordenada com as notas que ficaram acima da média;
    list -> list'''
    media=(sum(lista))/(len(lista))
    return (lista,media)