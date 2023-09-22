Def insere(lista_numero, n):
    """Função que dada uma lista ordenada(crescente) de numeros inteiros e um numero inteiro n,inclua n na posição correta, ou seja, de tal maneira que a lista continue ordenada.
    list, int -> list"""
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero