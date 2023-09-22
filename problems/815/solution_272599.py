def insere(lista_numero, n):
    """Dada uma lista ordenada de números inteiros e um número inteiro n, retorna a lista com o número n incluído na posição correta para que continue ordenada
    lista,int--> lista"""
    a=lista_numero
    a[0:0] = [n]
    list.sort(a)
    return a