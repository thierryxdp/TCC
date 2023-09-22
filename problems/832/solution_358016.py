def eh_quadrada(matriz):
    """Recebe uma matriz e retorna True se a matriz for quadrada e False se a matriz
       não for quadrada.
       list->bool

       Parameters:
       Matriz: Uma Matriz matemática"""
    if len(matriz)==0:
        return True
    else:
        if len(matriz)==len(matriz[0]):
            return True
        else:
            return False