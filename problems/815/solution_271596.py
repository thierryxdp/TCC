def insere(lista_numero, n):
    """Recebe uma lista ordenada e um número, e retorna
    uma lista com o número em seu devido lugar.
    list, int -> list"""
    x = lista_numero
    x.append(n)
    
    xordenado = list.sort(x)
    return xordenado