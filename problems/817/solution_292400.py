def acima_da_media(lista):
    '''Função que dada uma lista com as notas dos alunos,
    retorna uma nova lista somente com as notas
    dos alunos que ficaram acima da média.'''
    media=sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista,reverse=True)
    n=list.index(lista,media)
    lista_final=lista[0:n]
    list.sort(lista_final)
    return lista_final