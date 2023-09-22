def acima_da_media(lista):
    '''Função que dada uma lista com as notas dos alunos,
    retorna uma nova lista somente com as notas
    dos alunos que ficaram acima da média.'''
    media=sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    n=list.index(lista,media)
    lista_final=lista[n+1.1:]
    return lista_final