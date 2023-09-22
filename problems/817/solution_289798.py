def acima_da_media (lista):
    '''Funcao que, dada uma lista com as notas de uma turma, retorna uma lista ordenada com as notas que ficaram acima da media;
    list, int -> list'''

    media = sum(lista)/len(lista)

    if media in lista:
        list.sort (lista)
        L = list.index (lista, media)
        return lista [L+1:1]

    if media not in lista:
        lista.append (media) 
        list.sort (lista)
        L1 = list.index (media)
        return lista[L1+1:]