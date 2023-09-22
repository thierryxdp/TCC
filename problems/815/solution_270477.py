def insere(lista_numero,n):
    """Dada uma lista ordenada(crescente) de números inteiros
    e um número inteiro n, inclua n na posição correta, ou seja,
    de tal maneira que a lista continue ordenada;
    list,int -> list"""
    lista = lista_numero
    n = [n]
    z = list.append(lista,n)
    z = list.sort(lista)
    return z