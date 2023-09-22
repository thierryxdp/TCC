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


def acima_da_media(1):
    """Essa função irá retornar uma lista com as notas dos alunos que ficaram acima da média ; lista -> lista"""
    media = sum(1)/(1.0*len(1))
    aprovados = maiores(1,media)
    return aprovados