def insere(lista_numero,n):
    """Função que, dada uma lista ordenada (crescente) de números inteiros e um número inteiro n, inclui n na posição correta; lista,int->lista"""
    list.append(lista,n)
    list.sort(lista)
    lista_final = list.index(lista,n)
    return lista[lista_final+1:]