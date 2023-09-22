def acima_da_media(lista):
    '''função que dada uma lista com as notas dos alunos
    de uma turma, retorne uma lista ordenada com as notas
    que ficaram acima da média; list -> list'''
    media_alu=(sum(lista))/(len(lista))
    return maiores(lista, media_alu)