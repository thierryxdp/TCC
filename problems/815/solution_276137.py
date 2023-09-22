def insere(lista_numero,n):
    """Determinar uma lista odernada com um elemento n adicionado de forma que não mude o fator crescente da entrada;
    list, int - > list"""
    lista_numero += [n,]
    lista_numero.sort()
    return lista_numero