def acima_da_media(lista):
    '''acima_da_media recebe uma lista de nota dos alunos de uma turma e devolve uma lista ordenada com as notas que ficaram acima da média.
    list-->list'''
    list.sort(lista)
    tamanho_lista=len(lista)
    media=(sum(lista)//tamanho_lista)+1
    posicao=list.index(lista,media)
    return lista[posicao:]