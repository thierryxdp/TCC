def maiores(lista_inteiros, n):
    #list, int -> list
    
    list(lista_inteiros)
    lista_inteiros.append(n)
    lista_ordenada = sorted(lista_inteiros)
    entra_n = lista_ordenada.index(n)
    
    if n not in lista_ordenada:
        lista_inteiros.append(n)
    return lista_ordenada[entra_n + 1:]