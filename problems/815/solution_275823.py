insere(lista_numero,n):
    """Dada uma lista ordenanda de números inteiros e um número inteiro n, inclui n na posção correta. list -> list"""
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero