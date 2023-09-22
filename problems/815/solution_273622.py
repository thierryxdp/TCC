def insere(lista_numero,n):
    '''retorna n na posicao correta de maneira ordenada na lista
    list,int->list'''
    lista_numero.insert(1,n)
    return list.sort(lista_numero)