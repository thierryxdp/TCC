def acima_da_media(lista):
    """Funcao que dada uma lista com a notas dos alunos de uma turma,
    retorna uma lista ordenada com as notas qwue ficaram acima da media;
    list -> list"""


    list.sort(lista)
    media = sum(lista)/len(lista)
    
    if list.count(lista,media) >= 1:

        list.sort(lista)
        indice = list.index(lista,media)
        del lista[0:indice+1]
    
        return lista

    else:

        list.append(lista,media)
        list.sort(lista)
        indice = list.index(lista,media)
        del lista[0:indice+1]

        return lista