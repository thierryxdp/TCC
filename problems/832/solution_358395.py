def eh_quadrada(matriz):
    " " "Identifica se uma matriz é quadrada;lista, -> boolean " " "
    if len(matriz)==len(matriz[0]) or len(matriz)==0:
        return True
    else:
        return False