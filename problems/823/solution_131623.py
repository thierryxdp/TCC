def faltante(L):
    """Função descobre qual número inteiro de uma lista que esta faltando
       Parametro: list -> int"""
    contador = 1
    posicao = 0
    while contador <= len(L):
        if contador not in L:
            posicao= contador 
        contador = contador + 1
    if posicao == 0:
        posicao = contador
    return posicao