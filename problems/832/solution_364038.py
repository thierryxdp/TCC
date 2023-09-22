def eh_quadrada(mat):
    ''' Função que determina se uma matriz é quadrada ou não e conta 
    matrizes vazias como quadradas   matriz => True/False '''
     if any(len(linha) != len(mat) for linha in mat):
        return False

     for i in range(len(mat)):
        for j in range(i): # só vou até a diagonal
            if mat[i][j] != mat[j][i]:
                return False
        return True
     if len(mat)==0:
        return True