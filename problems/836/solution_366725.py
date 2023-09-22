#Dados um setor e uma matriz com as informações dos funcionários da empresa,
# esta função retorna todos os registros dos funcionários de tal setor, excluindo
# a informação contida na coluna de índice 2 da matriz.
# str, list(list) -> list(list)

def busca(setor, mat):
    resposta = []
    
    for i in range(len(mat)):
        if setor == mat[i][2]:
            info = []
            list.append(info,mat[i][0])
            list.append(info,mat[i][1])
            list.append(info,mat[i][3])
            list.append(resposta,info)
            
    return resposta