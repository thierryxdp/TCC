def faltante(lista):
    """Função que dada uma lista com N-1 inteiros numerados de 1 a N descubra qual número deste intervalo está faltando
    list -> int"""
    lista1N = list(range(1,len(lista)+2))
    i = 0
    while i < len(lista)+1:
        if lista1N[i] in lista:
            i = i+1
        else:
            return lista1N[i]