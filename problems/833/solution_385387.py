def conta_numero(numero,matriz):
    """Função que conta quantas vezes um determinado número aparace em uma matriz"""
    """Parâmetros de entrada:int,list"""
    """Parâmetros de saída:int"""
    contador=0
    for lista_interna in matriz:
        for item in lista_interna:
            if item ==numero:
                contador+=1
    return contador