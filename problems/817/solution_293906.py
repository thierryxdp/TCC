def acima_da_media(lista):
    '''Funcao que dada uma lista com as notas dos alunos de uma turma, retorna
    uma lista ordenada com as notas que ficaram acima da media
    list -> list'''
    media = sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    posicao = list.index(lista,media)
    maior = posicao + 1
    return lista[maior:]