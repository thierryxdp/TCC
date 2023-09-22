def insere(lista_numero: list, n: int)-> list:
    """Dada uma lista ordenada (crescente) de números inteiros e um número
    inteiro "n", a função inclue "n" na posição correta, de tal maneira
    que a lista continue na ordem crescente"""
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero