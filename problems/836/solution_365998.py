def busca (nome,matriz):
    dados = []
    for i in range (len(matriz)):
        if str.upper(nome) in str.upper(matriz[i][2]):
            dados += [[matriz[i][0] , matriz [i][1] , matriz [i][3]]]
    return dados