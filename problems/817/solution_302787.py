def acima_da_media(lista):
    '''Funcao que retorna uma lista com as notas dos alunos, de forma ordenada, daqueles que ficaram acima da media'''
    media=sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    tamanho=len(lista)
    a=list.index(lista,media)
    return lista[a:tamanho]