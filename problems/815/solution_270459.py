def insere(lista_numero,n):
    """Função que dada uma lista ordenada de forma
       crescente de números inteiros e um número
       inteiro n, inclui n na posição correta de tal
       forma que a lista continue ordenada.
       list -> list"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero