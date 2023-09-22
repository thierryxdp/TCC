def eh_quadrada(matriz):
    """função que booleana capaz de identificar se uma matriz é quadrada.OBS: matriz vazia é considerada quadrada
    list(list) -> bool"""
    
    if len (matriz) == 0:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else: 
        return False