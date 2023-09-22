def insere(lista_numero, n):
    """Retorna a sua lista em ordem crescente: list, int -> list"""
    y = int(n)
    lista_numero.append(y)
    return sorted(lista_numero)