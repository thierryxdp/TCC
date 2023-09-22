def eh_quadrada(matriz):
    '''Função que, dada uma matriz, diz se ela é uma Matriz
    Quadrada ou não;
    list->bool'''
    A=[]
    if matriz==[]:
        return True
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False