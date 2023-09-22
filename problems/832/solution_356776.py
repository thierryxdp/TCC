def eh_quadrada(matriz:list) -> bool:
    """Função que irá identificar se uma matriz é quadrada. Se a entrada for uma matriz vazia ela deverá ser identificada como quadrada.

        Parameters:
        matriz: matriz em formato de lista que deverá ser analisada

        Returns:
        valor booleano True caso seja quadrada ou False caso contrário

        list -> bool
    """


    if matriz == [[]]:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False