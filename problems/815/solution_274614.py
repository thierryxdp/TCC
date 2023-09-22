def insere(lista_numero,n):
    '''retorna n na posição correta dentro da lista_numero'''
    lista_numero = list.append(lista_numero,n)
    lista_resultado = list.sort(lista_numero)
    return lista_resultado