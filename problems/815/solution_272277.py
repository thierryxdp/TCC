def insere(lista_numero, n):
    """Dada uma lista ordenada de números inteiros e um número inteiro n, retorna a lista com o número n incluído na posição correta para que continue ordenada"""
    a = lista_numero
    a[0:0] = [n]
    b = list.sort(a)
    return b