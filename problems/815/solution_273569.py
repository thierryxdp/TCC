def insere(lista_numero,n):
    '''
    função que dada lista ordenada crescente como primeiro parametro, e um numero inteiro qualquer como segundo,
    retorna a lista com o número dado e organizada de forma crescente
    list--->list
    '''
    insere=list.append(lista_numero,n)
    organiza=list.sort(lista_numero)
    
    return lista_numero