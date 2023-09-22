insere(lista_numero,n):
    """dada uma lista ordenada crescente de números inteiros e um número n, inclua n na posição correta, lista, int--> lista"""
    lista_numero.append(n)
    list.sort(lista_numero)
    
    return lista_numero