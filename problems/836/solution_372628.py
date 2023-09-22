def busca(setor, matriz):
    resposta = []
    contatos = []
    for i in range(len(matriz)):
        if setor in matriz[i][2]:
            contatos = matriz[i][0] + matriz[i][1]+ matriz[i][3]
            resposta.append(contatos)
    return resposta