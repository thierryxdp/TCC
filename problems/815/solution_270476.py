def insere(lista_numero,n):
    """Dada uma lista ordenada(crescente) de números inteiros
    e um número inteiro n, inclua n na posição correta, ou seja,
    de tal maneira que a lista continue ordenada;
    list,int -> list"""
    lista = lista_numero
    n = [n]
    lista = list.append(lista,n)
    lista = list.sort(lista)
    return lista