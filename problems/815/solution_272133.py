def insere(lista_numero,n):
    """insere o int n na posição correta, de maneira que a lista continua ordenada;
    list, int -> list"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero