def eh_quadrada(matriz):
    """Funao que retorna se a matriz é ou não quadrada. List-->Bool"""
    count = 0
    for i in range(len(matriz)):
        if len(matriz) != len(matriz[i]) and len(matriz[0]) != 0:
            count += 1
    if count !=0:
        return False
    else:
        return True