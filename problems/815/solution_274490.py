def insere(lista_numero,n):
    '''Função que recebe a lista de entrada, e em seguida insere valor n de entrada na lista, depois 
    retorna a lista ordenada
    list,list→list'''
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero