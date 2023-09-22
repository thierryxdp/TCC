def eh_quadrada(matriz):
    " Verifica se a matriz é vaiza "
    if len(matriz) == 0:
        return True
    " Verifica se a matriz é quadrada "
    if len(matriz) == len(matriz[0]):
        return True
    " Caso os passo anteriores estajam errado, retorna Falso "
    else:
        return False