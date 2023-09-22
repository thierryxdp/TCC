def insere(lista_numero,n):
    '''insere um numero na lista mantendo sua ordem crescente. list,int->list'''
    lista_numero.append(n)
    return list.sort(lista_numero)