def busca(setor, matriz):
    resposta = []
    contatos = []
    for i in range(len(matriz)):
        if setor in matriz[i][2]:
            for j in (0,1,3):
                contatos.append(matriz[i][j])
            resposta.append(contatos)
    return resposta