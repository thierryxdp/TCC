def busca(setor, matriz):
        #busca um usuario baseado no seu setor dentro da empresa.
        #entrada: setor: de busca ; matriz : matriz
        #saida: res: matriz com usuarios do setor
    res = []
    for i in range(0, len(matriz)):
        for o in range(0, len(matriz[i])):
            if setor.lower() == matriz[i][o].lower():
                dados = matriz[i].copy()
                dados.pop(dados.index(dados[o]))
                res.append(dados)
    return res