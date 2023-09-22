def acima_da_media(lista):
    '''função que dada uma lista com as notas de alunos retorna aquela acima da média;
    list->list'''
    media = sum(lista)/len(lista)
    list.append (lista,media)
    list.sort (lista)
    a = list.index (lista, media)
    indice  = a+1
    return lista[indice:]