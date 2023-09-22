def conta_numero(numero,matriz):
    """Função que conta quantas vezes um determinado número aparace em uma matriz"""
    """Parâmetros de entrada:int,list"""
    """Parâmetros de saída:int"""
    contador=0
    n_linha=0
    for linha in matriz[n_linha]:
        contador+=1
    n_linha+=1
    return contador