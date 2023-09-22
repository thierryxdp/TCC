def insere(lista_numero,n):
    """retorna a inserção de um número inteiro n na lista_numero,da forma que ela continue ordenada; list,int-->list"""
    lista_numero = list.append(lista_numero,n)
    x = list.sort(lista_numero)
    return x