def insere(lista_numero,n):
    """dada uma lista ordenada (crescente) de números inteiros e um número inteiro n, inclua n na posição correta, ou seja, de tal maneira que a lista continue ordenada."""
    lista_numero=list.sort(lista_numero)
    indice=list.index(lista_numero,n)
    lista_numero= list.insert(lista_numero,indice,n)
    return lista_numero