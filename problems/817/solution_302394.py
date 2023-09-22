def acima_da_media(lista_numero):
    '''função que retorna a nota dos alunos em uma lista ordenada com apenas as notas acima 
    da média'''
    n=((sum(lista_numero))/len(lista_numero))
    list.append(lista_numero, 6)
    list.sort(lista_numero)
    a=list.index(lista_numero,6)
    return lista_numero[a+1:]