def conta_numero(numero,matriz):
    """Função que conta quantas vezes um determinado número aparace em uma matriz"""
    """Parâmetros de entrada:int,list"""
    """Parâmetros de saída:int"""
    contador=0
    for elemento in matriz:
        if elemento==numero:
            contador+=1
    return contador