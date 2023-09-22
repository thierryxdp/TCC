def faltante (lista_pecas):
    """Função que descobre e retorna a peça faltante do jogo"""
    """Parâmetros de entrada: list"""
    """Parâmetros de saída: int"""
    contador=1
    indice=0
    while contador >= lista_pecas[indice]+1:
        contador+=1
        indice+=1
    return contador