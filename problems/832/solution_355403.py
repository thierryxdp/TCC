def eh_quadrada(matriz):
    """Função que retorna se a matriz dada como parâmetro é quadrada;
    list -> bool"""
    if len(matriz) == 0 or len(matriz) == len(matriz[0]):
        return True
    else:
        return False