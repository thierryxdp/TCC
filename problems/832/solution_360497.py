def eh_quadrada(matriz):
    """Recebe uma matriz e retorna se a mesma é quadrada ou não.
    	lista -> booleano"""
    for i in matriz:
        if len(i) == len(matriz):
            value = True
        else:
            value = False
    
    if len(matriz) == 1 and len(matriz[0]) == 0:
        value = True
    return value