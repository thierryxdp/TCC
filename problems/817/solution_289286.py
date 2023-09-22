def acima_da_media(lista):
    '''Função que, dada uma lista com as notas de alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da média; list -> list'''
    media = sum(lista)/len(lista)
    if media in lista:
        list.sort(lista)
        posicao= list.index(lista,media)
        return lista[posicao+1:]
    else:
        lista=lista+[media]
        list.sort(lista)
        posicao= list.index(lista,media)
        return lista[posicao+1:]