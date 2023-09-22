def maiores(lista_inteiros, n):
    #list, int -> list
    list(lista_inteiros)
    lista_inteiros.append(n)
    lista_ordenada = sorted(lista_inteiros)
    
    return lista_ordenada