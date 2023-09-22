def insere(lista_numero, n):
    """Funcão que retorna uma lista em ordem crescente, contendo "lista_numero" e "n".
    list, list -> list"""
    a= lista_numero
    list.extend(lista_numero, [n])
    a.sort()
    return a