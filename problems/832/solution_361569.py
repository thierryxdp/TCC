def eh_quadrada(matriz):
    '''funcao que recebe uma matriz como entrado e identifica se ela e quadrada ou nao
list(list) -> bool'''
    if len(matriz)==len(matriz[0]):
        return True
    elif matriz==[]:
        return True
    else:
        return False