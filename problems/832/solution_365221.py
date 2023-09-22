def eh_quadrada (matriz):
    'função que recebe uma matriz e identifica se é ou não quadrada. int->str'
    if matriz==[]:
        return True
    return len(matriz)==len(matriz[0])