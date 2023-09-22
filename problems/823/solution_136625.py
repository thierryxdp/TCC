def faltante (lista_pecas):
    """Função que descobre e retorna a peça faltante do jogo"""
    """Parâmetros de entrada: list"""
    """Parâmetros de saída: int"""
    contador=1
    indice=0
    ordenada=lista_pecas.sort()
    while contador >= ordenada[indice]:
        contador+=1
        indice+=1
    return contador