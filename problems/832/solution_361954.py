def eh_quadrada (matriz):
    '''
        Função que recebe uma matriz (matriz) e retorna
        True caso ela for quadrada e False caso o contratio;
        list -> bool
    '''
    if matriz==[]:
        matriz=[[1]]
    return len(matriz)==len(matriz[0])