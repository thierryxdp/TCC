def busca(setor,matriz):
    'Busca as informacaoes dos funcionarios que trabalham no setor escolhido'
    'str, lista -> lista'
    dados=[]
    for i in range(len(matriz)):
        if matriz[i][2]==setor:
            list.pop(matriz[i],2)
            dados.append(matriz[i])
    return dados