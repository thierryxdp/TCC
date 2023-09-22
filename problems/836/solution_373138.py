def busca(setor, matriz):
    dados = []
    
    for i in range(len(matriz)): ##percorre até o range da matriz
        if setor in matriz[i]: ##se o setor estiver nessa posição
            list.append(dados, matriz[i]) ##é colocado na lista de dados
    for j in range(len(dados)): ##percorre o range dos dados
        if dados[j][2] == setor: ##se estiver, é excluído
            del dados[j][2]
        
    return dados