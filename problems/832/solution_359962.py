def eh_quadrada(matriz):
    """Função que ao receber uma lista em formato de matriz, retorna
    se a matriz dada é quadrática ou não;
    list -> bool"""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if len(matriz[i]) == len(matriz):
                return True
            else:
                return False
    if len(matriz) == 0:
        return True