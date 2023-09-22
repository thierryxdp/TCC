def eh_quadrada(matriz):
    """
    Função que recebe uma matriz e retorna True caso ela
    seja quadrada e False caso não seja
    """
    if len(matriz)==0:
        return True
    return len(matriz)==len(matriz[0])