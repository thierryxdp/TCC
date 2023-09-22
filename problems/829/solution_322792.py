def soma_h(n):
    """Função que calcula a soma de 1+1/2+1/3+...+1/n"""
    """Parâmetros de entrada: int"""
    """Parâmetros de saída: float"""
    acumulador=0
    for numero in range(1,n+1):
        acumulador+=n/numero
    return round(acumulador,2)