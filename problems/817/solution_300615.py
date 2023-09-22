def acima_da_media(lista):
    '''
    função que dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da média;
    list -> list
    '''
    media = sum(lista)/len(lista)
    if list.count(lista,media) == 0:
        list.insert(lista,1,media)
        list.sort(lista)
        a = list.index(lista,media)
        nova_lista = lista[a+1:]
        return nova_lista
    elif list.count(lista,media) > 0:
        list.sort(lista)
        a = list.index(lista,media)
        nova_lista = lista[a+1:]
        return nova_lista