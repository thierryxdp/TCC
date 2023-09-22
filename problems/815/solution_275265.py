def insere(lista_numero,n):
    '''Dada uma lista ordenada de números inteiros e um
    número inteiro n, a função inclui n na lista de modo a
    manter a lista ordenada do menor valor para o maior.
    list,int -> list'''
    if n not in lista_numero:
        list.append(lista_numero,n)
        list.sort(lista_numero)
        return lista_numero
    else:
        return lista_numero