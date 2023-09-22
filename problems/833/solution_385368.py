def conta_numero(numero,matriz):
    """Função que conta quantas vezes um determinado número aparace em uma matriz"""
    """Parâmetros de entrada:int,list"""
    """Parâmetros de saída:int"""
    contador=0
    n_linha=0
    n_matriz=0
    for elemento in matriz[n_matriz]:
        if elemento==numero:
            contador+=1
        n_matriz+=1
    return contador