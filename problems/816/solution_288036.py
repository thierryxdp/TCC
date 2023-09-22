def maiores(*args):
    """Função que retorna uma lista com todos os elementos maiores que (n).
    Use list: list[list, int] -> list
    list -> list"""
    nova_lista = args[0]
    n = args[1]
    nova_lista.append(n)
    if max(nova_lista) == n:
        return []
    else:
        lista_decrescente = sorted(nova_lista, reverse=True)
        index_n = lista_decrescente.index(n)
        return sorted(lista_decrescente[:index_n])