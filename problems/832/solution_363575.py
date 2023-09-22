def eh_quadrada(matriz):
    '''Verifica se a matriz é no formato quadrado;
    list(list)->bool'''
    
    for i len(matriz):
        for j len(matriz[0]):
            if i len(matriz)== j len(matriz[0]):
                return True
            else:
                False