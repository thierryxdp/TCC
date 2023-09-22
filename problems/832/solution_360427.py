def eh_quadrada(matriz):
    '''Função que consegue indentificar se a matriz é 
    quadrada ou não
    entrada=list
    saida=bool'''
    if len(matriz)==0 or len(matriz)==len(matriz[0]):
        return True
    else:
        return False