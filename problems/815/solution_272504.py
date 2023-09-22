def insere(lista_numero,n):
    """
    Dada uma lista ordenada (crescente) de numeros inteiros e um numero
    inteiro n, inclua n na posição correta;
    list, int -> list
    """
    return lista_numero(:n-1) + [n] + lista_numero(n+1:)