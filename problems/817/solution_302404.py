def acima_da_media(li,n):
    '''Dada uma lista com as notas dos alunos de uma turma, retorna
    uma lista ordenada com as notas que ficaram acima da média.
    list, int --> list'''
    media = (sum(li))/(len(li))
    return maiores(li,n)