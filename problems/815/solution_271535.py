def insere(lista_numero, n):
    '''retorna uma lista com um novo termo 'n' de ordem
    crescente
    list,int->list'''
    lista=lista_numero+[n]
    list.sort(lista)
    
    return lista