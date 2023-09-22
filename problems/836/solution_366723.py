def busca(setor, mat):
    resposta = []
    
    for i in range(len(mat)):
        if setor == mat[i][2]:
            info = [mat[i][0:2]]
            list.append(info,mat[i][3])
            list.append(resposta,info)
            
    return resposta