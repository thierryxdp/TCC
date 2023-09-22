def insere(lista_numero,n):
    '''função que dada uma lista crescente inclui o numero n na posição correta para que a lista
    continue ordenada; list,int->list''' 
    list.sort(lista_numero)
    list.append(lista_numero,n)
    return lista_numero