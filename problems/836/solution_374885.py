def busca(setor, matriz):
    dados = []
    lista = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
           dados.append(matriz[i])
    for j in range(len(dados)):
        if dados[j][2] == setor:
           del dados[j][2]
    if dados ==  lista:
        return 'Nenhum Registro'
    return dados