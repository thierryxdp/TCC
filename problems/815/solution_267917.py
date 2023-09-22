def insere (lista_numero, n):
    """Função que dada uma lista ordenada (crescente) e um número n inteiro, insere-o na lista na posição correta;
       list, int -> list."""
    list.insert (lista_numero, 0, n)
    list.sort (lista_numero)
    return lista_numero