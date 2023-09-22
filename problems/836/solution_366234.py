def busca (setor, matriz):
    matriz_nova = []
    para_acrescentar = []
    linhas = len(matriz)
    
    for i in range(linhas):
        if matriz[i][2] == setor:
            para_acrescentar.append(i)
    count = 0
    
    for i in para_acrescentar:
        matriz_nova.append(matriz[i])
        count += 1
    
    for i in range(len(matriz_nova)):
        matriz_nova[i].remove(setor)
    return matriz_nova