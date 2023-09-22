def acima_da_media(lista):
    '''função que dada uma lista com as notas
    retorna uma lista ordenada com as notas acima da média.   
    append : adiciona um único item a lista existente.
    sort : organiza a lista em ordem crescente por padrão.
    index : returna a posição da primeira ocorrência do valor em
    específico.
    lista -> lista'''
    
    media=sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    tamanho=len(lista)
    na_media=list.index(lista,media)
    return lista[na_media+1:tamanho]