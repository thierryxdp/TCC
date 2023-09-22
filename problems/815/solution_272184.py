def insere(lista_numero,n):
    """função que dada uma lista ordenada(crescente) de números 
    inteiros e um número inteiro n, inclua n na posição
    correta para que a lista continue ordenada"""
    lista_numero.append(n)
    list. sort(lista_numero)
    return lista_numero