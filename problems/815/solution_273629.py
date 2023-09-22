def insere(lista_numero,n):
    '''retorna n na posicao correta de maneira ordenada na lista
    list,int->list'''
    lista_numero.append(n)
    lista_numero=list.sort(lista_numero)
    return lista_numero