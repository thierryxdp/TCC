def fatorial(numero):
    """Função que calcula e retorna o fatorial de um número"""
    """Parâmetro de entrada: int"""
    """Parâmetro de saída: int"""
    contador=1
    acumulador=1
    while numero>=contador:
        acumulador*=contador
        contador+=1
    return acumulador