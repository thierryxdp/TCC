def eh_quadrada(mat):
    '''Função que recebe uma matriz(mat);
identifica se a matriz é quadrada, ou seja, sem linha e nem coluna;
retorna True se for quadrada e False caso contrário.
matriz->bool'''
    for l in mat:
        for ij in l:
            if ij<0:
                    return True
    return  False