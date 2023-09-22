def eh_quadrada(matriz):
    """Dada a uma matriz a função retorna True
    se a matriz for quadrada e False caso não seja
    Parametros de Entrada: list
    Retorna: bool"""
    elementos=0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            elementos= elementos+1
    if len(matriz)==0:
        return True
    elif (elementos/len(matriz))== len(matriz):
        return True
    else:
        return False