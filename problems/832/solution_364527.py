def eh_quadrada(matriz):
    '''Função que identifica se uma matriz é quadrada;
       list => Bool'''
    for i in matriz:
        for e in i:
            if len(e) == len(i):
                return True
            if  len(e) != len(i):
                return False