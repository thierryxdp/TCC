def insere (lista, numero):
    """funcao que dada uma lista ordenada de numeros inteiros e um numero inteiro, inclui o numero na posicao adequada
    list -> list"""
    lista.append (numero)
    lista.sort ()
    return lista