def insere(lista_numero,n):
    """Retorne uma lista odernada com um elemento n adicionado de forma de não alterar o fator crescente da entrada;
    list, int - > list"""
    lista_numero += [n,]
    return lista_numero.sort()