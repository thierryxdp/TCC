def insere(lista_numero, n):
    """funcao que dada uma lista ordenada e um numero inteiro, inclua o numero na posicao correta"""
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero