def acima_da_media(lista):
    """Funçao que dada uma lista com as notas dos alunos de uma turma, 
    retorna uma lista ordenada com as notas que ficam acima da média;
    list-->list"""
    media = sum(lista)/len(lista)
    if len(lista) == 1:
        list.clear(lista)
        return lista
    elif media in lista:
        list.sort(lista)
        index = list.index(lista,media)
        return lista[index+1:]
    else:
        list.append(lista,media)
        list.sort(lista)
        listafinal = list.index(lista,media)
        return lista[listafinal+1:]