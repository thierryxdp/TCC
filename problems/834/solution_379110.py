def samuel_n_elementos(mat):
    linhas = len(mat)
    colunas = len(mat[0])
    return linhas * colunas

def soma_no_todo(mat):
    soma = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            soma += mat[i][j]
    return soma

def media_matriz(mat):
  return soma_no_todo(mat) / samuel_n_elementos(mat)