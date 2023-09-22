def busca(setor, matriz):
    setor = []
    lista = []
    for i in range(len(matriz)):
        if setor in matriz[i]:
           dados.append(matriz[i])
    for j in range(len(dados)):
        if dados[j][2] == setor:
           del dados[j][2]
    if setor ==  lista:
        return 'Nenhum Registro'
    return setor