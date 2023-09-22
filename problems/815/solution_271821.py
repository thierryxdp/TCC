def insere(lista_numero,n):
    """
    Função que dada uma lista ordenada(crescente) de números inteiros
    e um número inteiro n, inclua n na posição da lista de tal maneira
    que a lista continue ordenada.
    lista, int -> lista
    """
    n=[n]
    numeros=lista_numero+n
    list.sort(numeros)
    return numeros