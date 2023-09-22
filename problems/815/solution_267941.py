def insere(lista_numero, n):
    """dada uma lista ordenada (crescente) de números inteiros e um número inteiro n, a funão inclui n na lista e a 
    retorna de forma que permaneça ordenada; list, int -> list"""
    lista_numero[0:0] = [n]
    list.sort(lista_numero)
    return lista_numero