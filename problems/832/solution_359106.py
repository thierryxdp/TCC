def eh_quadrada(matriz: list)-> bool:
    """Dada uma matriz, a função retorna True se a matriz for quadrada
    ou False, caso ela não seja quadrada"""
    numlinhas = len(matriz)
    numcolunas = len(matriz[0])
    if matriz == []:
        return True
    elif numlinhas == numcolunas:
        return True
    else:
        return False