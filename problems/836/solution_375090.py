def busca(are,mat):
    """Função que recebe área profissional e retorna todos os dados dos funcionários dessa área.
signature: string, matrix -->  matrix """
    nma = []
    for i in range(len(mat)):
        if mat[i][2] == are:
            nma = nma + [mat[i]]
    return nma