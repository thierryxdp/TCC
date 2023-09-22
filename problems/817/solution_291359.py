def acima_da_media(lista):
    '''Função que recebe uma lista com notas dos alunos e
    retorna uma lista ordenada com as notas que ficaram 
    acima da média; list -> list'''
    if 5 in lista and list.count(lista, 5) < 2:
        list.sort(lista)
        return lista[list.index(lista, 5):]
    elif 5 in lista and list.count(lista, 5) >= 2:
        list.sort(lista)
        return lista[list.index(lista, 5)+list.count(lista, 5)-1:]
    else:
        list.append(lista, 5)
        list.sort(lista)
        return lista[list.index(lista, 5)+1:]