def insere(lista_numero,n):
    """funcao que dada uma lista ordenada de numeros inteiros e um numero inteiro n,inclue n na posicao correta;str,str-.list """
    n=[n]
    lista = lista_numero + n
    lista.sort()
    return lista