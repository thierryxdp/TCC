def acima_da_media(lista):
    ''' Função que, dada uma lista com as notas dos alunos de uma turma,
retorna uma lista ordenada com as notas que ficaram acima da media.
    list,float-->list'''
    list.sort(lista)
    if media in lista:
        posicao = list.index(lista,5)
        del lista[0:posicao]
        return lista
    if media not in lista:
        list.append(lista,5)
        list.sort(lista)
        posicao = list.index(lista,5)
        del lista[0:posicao+1]
        return lista