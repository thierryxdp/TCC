def soma_h(inteiro):
    """Funcao que calcula e retorna o resultado da equação passada
    anteriormente com base em um numero inteiro.
    Entrada: int;
    Saida: float;
    
    Parameter:
    inteiro: Numero inteiro para ser usado na equação.
    """
    H = 0
    
    for divisor in range(1, inteiro + 1):
        if (divisor <= inteiro):
            H += 1 / divisor
    return H.round(2)