def insere(lista_numero,n):
    """funcao que dada uma lista ordenada(crescente) de numeros inteiros e
um numero inteiro n, inclua n na posicao correta, de forma que a lista continue
ordenada
list,int->list"""
    lista_inserida = lista_numero + [n]
    list.sort(lista_inserida)
    return lista_inserida