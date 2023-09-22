def busca(matriz, setor):
    
    for linha in range(len(matriz)):
        if matriz[linha][2] == setor:
            return matriz[linha]