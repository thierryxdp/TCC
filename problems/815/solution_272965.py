def insere(lista_numero, n):
    "Dada uma lista de números inteiros e um número inteiro n, inclui esse número na posição ordenada na lista; list or tuple, int -> list"
    lista_numero = list(lista_numero)
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero