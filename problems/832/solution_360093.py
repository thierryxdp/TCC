def eh_quadrada(matriz: list) -> bool:
    """Essa função, dada uma matriz como parâmetro de entrada,
    determina se é uma matriz quadrada(True) ou não(False)."""
    if matriz == []:
        return True
	
    elif len(matriz) == len(matriz[0]):
        return True
    
    else:
        return False