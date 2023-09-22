def faltante(L):
    """função que retorna qual peça esta faltando
    em um jogo de quebra-cabeça."""
    lista = list(range(1,len(L)+5))
    index = 0
    list.extend(L, [0,0,0])
    while lista[index] == L[index]:
        index += 1
    return lista[index]