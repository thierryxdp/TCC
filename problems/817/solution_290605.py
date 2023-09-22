def acima_da_media(lista):
    '''Função que retorna as notas dos alunos que ficaram acima da média;
    list -> list'''
    l=(sum(lista)//len(lista))
    list.append(lista,l)
    list.sort(lista)
    i=list.index(lista,l)
    del lista[:i+1]
    return lista