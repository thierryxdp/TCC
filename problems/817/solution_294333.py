def acima_da_media(lista):
    """Funcao que dada uma lista com a notas dos alunos de uma turma,
    retorna uma lista ordenada com as notas qwue ficaram acima da media;
    list -> list"""

    if list.count(lista,50) >= 1:
    
        list.sort(lista)
        indice = list.index(lista,50)
        del lista[0:indice+1]
    
        return lista

    elif list.count(lista,50) == 0:
    
        list.append(lista,50)
        list.sort(lista)
        indice = list.index(lista,50)
        del lista[0:indice+1]
    
        return lista