def eh_quadrada(mat):
    '''Função que recebe uma matriz(mat);
identifica se a matriz é quadrada, ou seja, sem linha e nem coluna;
retorna True se for quadrada e False caso contrário.
list(list)->bool'''
    if len(mat)==0:
        return True 
    elif len(mat)==len(mat[0]):
        return True
    else:
        return False