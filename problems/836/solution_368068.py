def busca(palavra,matriz):

    dados = []

    for i in range(len(matriz)):
        
        if palavra in matriz[i]:
            contato = matriz[i][0],matriz[i][1],matriz[i][3]
            list.append(dados,contato)

    return dados