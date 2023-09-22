def insere(lista_numero, n):
    """Dada uma lista ordenada, crescente, de números inteiros e um número inteiro n,
    inclua n na posição correta, de modo que ela continue ordenada;
    list, int -> list"""
    lista_nova = lista_numero.append(n).sort()
    return lista_nova