def acima_da_media(lista):
    '''função que dada uma lista com as notas dos alunos de uma
    turma,retorna uma lista ordenada coma as notas que ficaram 
    acima da média; list-->list'''
    n=len(lista)
    media=(sum(lista))/n
    list.append(lista,media)
    list.sort(lista)
    x=list.index(lista,media)
    return lista[x+1:]