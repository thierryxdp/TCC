def insere(lista_numero, n):
    """Função que recebe uma lista ordenada de numeros inteiros e um numero inteiro n,
    retornando uma lista ordenada com o numero n na posição correta
    entrada: lista, int
    retorno: lista"""
    lista_numero.insert(0,n)
    lista_numero.sort()
    return lista_numero