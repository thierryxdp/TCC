def eh_quadrada(matriz):
    '''Função que recebe uma matriz e identifica se ela é 
    quadrada ou não.
    assinatura: list -> bool'''
    if len(matriz) == 0 or len(matriz) == len(matriz[0]): 
        return True
    else:
        return False