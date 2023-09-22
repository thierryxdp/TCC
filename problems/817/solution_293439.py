def acima_da_media(notas):
    '''Função que recebe uma lista com as notas dos alunos de uma turma.
    Retorna uma lista ordenada com as notas que ficaram acima da média;
    list -> list'''
    soma_notas = sum(notas)
    qtd_notas = len(notas)
    media = soma_notas / qtd_notas
    acima_media = [x for x in notas if x > media]
    list.sort(acima_media)
    return acima_media