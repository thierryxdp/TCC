def eh_quadrada(matriz):
    "Função que ao receber uma matriz retorna um valor booleano indicando se a matriz é quadrada. list --> bool"
    if len(matriz)== 0 or len(matriz)== len(matriz[0]):
        return True
    else:
        return False