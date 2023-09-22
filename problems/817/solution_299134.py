def acima_da_media(lista):
    '''Função que dada uma lista com as notas dos alunos retorna 
    outra lista ordenada com as notas acima da média
    list -> list'''
    lista1 = sum(lista)
    lista2 = len(lista)
    lista3 = (lista1/lista2)
    list = lista
    if lista3 in list:
        list.remove(lista3)
    list.append(lista3)
    list.sort()
    return list[(list.index(lista3) + 1):]