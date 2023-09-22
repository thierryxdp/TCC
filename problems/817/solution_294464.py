def acima_da_media(m):
    '''função que dada uma lista com as notas
    dos alunos retorne uma lista ordenada com as notas que
    ficaram acima da média. list > list'''
    media = sum(m)/len(m)
    m2 = [i for i in m if i >= media]
    m2.sort()
    return m2