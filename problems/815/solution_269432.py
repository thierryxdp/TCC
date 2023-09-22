def insere (lista_numero: list, n: int) ->int:
    """Retorna a lista_numero com o numero inteiro n, em ordem crescente."""
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero