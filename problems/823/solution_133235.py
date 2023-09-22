def faltante (lista_peca):
    """Função que retorna o numero de peças faltantes de um quebra-cabeça
    list -> int"""
    lista = []
    x = 0
    lista_peca.sort()
    while x < (len(lista_peca)-1):
        if lista_peca[x+1] - lista_peca[x] > 1:
            return x + 2
        x = x + 1
    if lista_peca[0] == 1:
        return lista_peca[-1]+1
    else:
        return lista_peca[0]-1