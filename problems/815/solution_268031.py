def insere(lista_numero, n):
    """Função que ao receber uma lista em ordem crescente insere o numero inteiro n na posição correta; lista, int -> lista"""
    x = list.append(lista_numero, n)
    list.sort(x)
    return x