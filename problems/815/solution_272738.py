def insere(lista_numero,n):
    """
    Dada uma lista ordenada (crescente) de numeros inteiros e um numero
    inteiro n, inclua n na posição correta;
    list, int -> list
    """
    lista = lista_numero.append(n)
    lista = list.sort(lista)
    return lista