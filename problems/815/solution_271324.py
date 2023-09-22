def insere(lista_numero,n):
    """funcao que, dada uma lista ordenada em ordem crescente de numeros inteiros e um numero n, inclua n na posicao correta, com a lista permanecendo ordenada
    list(int),int--->list(int)"""
    lista_numero=lista_numero+[n]
    list.sort(lista_numero)
    return lista_numero