def insere(lista_numero,n):
    """Retornar uma lista odernada com um elemento x adicionado de forma que não altere o fator crescente da entrada;
    list, int - > list"""
    lista_numero += [x,]
    lista_numero.sort()
    return lista_numero