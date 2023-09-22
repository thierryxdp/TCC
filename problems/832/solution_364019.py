def eh_quadrada(mat):
if mat = []:
            return True
        
     if any(len(linha) != len(mat) for linha in mat):
        return False

     for i in range(len(mat)):
        for j in range(i): # só vou até a diagonal
            if mat[i][j] != mat[j][i]:
                return False
        return True