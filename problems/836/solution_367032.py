def busca(setor, matriz):
    encontrado = []
    
    for linha in range(len(matriz)):
        if matriz[linha][2] == setor:
            encontrado += [matriz[linha][0], matriz[linha][1], matriz[linha][3]] 
    return encontrado