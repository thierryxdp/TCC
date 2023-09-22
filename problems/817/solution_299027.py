def acima_da_media(lista):
    """funçao que dada uma lista com notas de alunos de uma turma, retorna uma lista em ordenada com as notas maiores para menores; list->list"""
    
    lista1 = sm(lista)
    lista2 = len(lista)
    lista3 = lista1/lista2
    
    list=lista
    if lista3 in list:
        list.remove(lista3)
    list.append(lista3)
    list.sort()
    return list[(list.index(lista3)+1):]