def insere(lista_numero,n):
    """
    dada uma lista crescente de números inteiros e um outro número
    inteiro, retorna uma nova lista crescente incluindo o outro número.
    """
    
    lista2=lista_numero + [n]
    list.sort(lista2)
    return lista2