def acima_da_media(l):
    '''
    Função que dada uma lista comas notas dos alunos de uma turma, retorna uma lista
    ordenada com as notas que ficaram acima da media
    list-> list
    '''
    list.sort(l)
    media = (sum(l))/ (len(l))
    return media