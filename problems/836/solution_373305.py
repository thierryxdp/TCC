def busca(setor, matriz):
    nova = []
    
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            dados = matriz[i][0:2]+matriz[i][3:]
            nova = nova + [dados]
    
    return nova