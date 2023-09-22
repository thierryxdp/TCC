def acima_da_media(lista):
    '''função que dada uma lista com as
    notas dos alunos retorna uma lista ordenada
    com as notas acima da média.
    append : adiciona um único item à lista.
    sort : organiza a ordem em lista crescente.
    index : retorna a posição da primeira ocorrência
    do valor em específico
    lista -> lista'''

    media = sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    na_media=list.index(lista,media)
    return lista[na_media+1:len(lista)]