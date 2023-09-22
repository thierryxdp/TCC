def eh_quadrada(matriz):
    """Retorna se a matriz é quadrada;
       Entrada: list;
       Saída: bool;
    """
    if len(matriz)==len(matriz[0]):
        return True
    if len(matriz) == 0:
        return True
    else: 
        return False