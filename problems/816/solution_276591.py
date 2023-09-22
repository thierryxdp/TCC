def maiores(lista_de_numeros_decrescente,n):
    """blabla"""
    list.reverse(lista_de_numeros_decrescente)
    lista_de_numeros_decrescente = list.insert(lista_de_numeros_decrescente,n)
    list.reverse(lista_de_numeros_decrescente)
    primeira_posicao = list.index(lista_de_numeros_decrescente,n)
    return lista_de_numeros_decrescente[:primeira_posicao]