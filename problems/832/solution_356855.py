def eh_quadrada(matriz):
    """Retorna se a matriz é quadrada;
       Entrada: list;
       Saída: bool;
    """
    if len(matriz)==len(matriz[0]):
        return True
    if matriz == []:
        return True
    else: 
        return False