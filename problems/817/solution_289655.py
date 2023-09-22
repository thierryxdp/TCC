def acima_da_media(lista):
    ''' Função que, dada uma lista com as notas dos alunos de uma turma,
retorna uma lista ordenada com as notas que ficaram acima da media.
    list,float-->list'''
    list.sort(lista)
    media = sum(lista)/len(lista)
    if media in lista:
        posicao = list.index(lista,media)
        del lista[0:posicao]
        return lista
    if media not in lista:
        list.append(lista,media)
        list.sort(lista)
        posicao = list.index(lista,media)
        del lista[0:posicao+1]
        return lista