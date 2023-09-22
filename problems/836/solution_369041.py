def busca(setor,mat):
    '''Função que recebe uma str(setor) que indica o setor a ser avaliado;
uma matriz(mat) contendo: nome, registro, setor e telefone de um funcionário;
(todas em formato str). Faz a busca por setor e retorna dados referentes aos funcionários deste setor.
str,list(list)->list'''
    f = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if setor in mat[i][j]:
                f.append(mat[i])
    return f