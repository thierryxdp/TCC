def faltante (lista_pecas):
    """Função que descobre e retorna a peça faltante do jogo"""
    """Parâmetros de entrada: list"""
    """Parâmetros de saída: int"""
    contador=0
    pecas_q_faltam=1
    lista_pecas.sort()
    while contador < len(lista_pecas):
        if pecas_q_faltam==lista_pecas[contador]:
        	pecas_q_faltam+=1
        contador+=1
    return pecas_q_faltam