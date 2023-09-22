def busca(setor,mat):
    resposta = []
    for i in range (len(mat)):
            if mat[i][2] == setor:
                    z = mat[i][:2] + mat[i][3:]
                    list.append(resposta,z)
                    return resposta