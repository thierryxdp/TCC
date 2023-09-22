def eh_quadrada(matriz):
    '''Função que identifica se uma matriz é quadrada;
       list => Bool'''
    externo = []
    
    if len(matriz) == 0:
        return True
    
    for i in matriz:
        externo.append(i)
        interno = []
        for e in i:
            interno.append(e)
 
    if len(externo) == len(interno):
        return True
    if len(externo) != len(interno):
        return False