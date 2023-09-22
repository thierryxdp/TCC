def eh_quadrada(mat):
    '''Função que recebe uma matriz(mat);
identifica se a matriz é quadrada, ou seja, sem linha e nem coluna;
retorna True se for quadrada e False caso contrário.
matriz->bool'''
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]<0 or mat[i][j]==[]:
                return True
    return False