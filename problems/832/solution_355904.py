def eh_quadrada (matriz):
    if matriz==[[]]:
        return True
    linha1=matriz[0]
    if len(linha1)==len(matriz):
        return True
    else:
        return False