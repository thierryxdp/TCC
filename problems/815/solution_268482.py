def insere(lista_numero,n):
    """dada uma lista crescente de inteiros, acrescenta o número n na posição correta
    list, int->list"""
    list.extend(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero