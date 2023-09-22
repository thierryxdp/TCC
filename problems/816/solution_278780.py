def maiores(lista, numero):
    """Função que retorna uma lista com todos os elementos maiores que (n).
    Use list: list[list, int] -> list
    list -> list"""
    lista.append(numero)
    if max(lista) == numero:
        return []
    else:
        lista_decrescente = sorted(lista, reverse=True)
        index_n = lista_decrescente.index(numero)
        return sorted(lista_decrescente[:index_n])