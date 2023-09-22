def acima_da_media(lista):
    '''dada uma lista com as notas dos alunos de uma turma 
    retorna uma lista ordenada com as notas que ficaram acima da média
    lista->lista'''
    
    media=sum(lista)/len(lista)

    list.sort(lista)

    posicao=list.index(lista,media)

    return lista[posicao+1:]