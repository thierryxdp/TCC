def acima_da_media(lista):
    '''dada uma lista com as notas dos alunos de uma turma 
    retorna uma lista ordenada com as notas que ficaram acima da média
    list->list'''
    
    media=sum(lista)/len(lista)

    if media in lista:

        list.sort(lista)

        posicao=list.index(lista,media)

        return lista[posicao+1:]

    else:

        list.append(lista,media)

        list.sort(lista)

        posicao=list.index(lista,media)

        return lista[posicao+1:]