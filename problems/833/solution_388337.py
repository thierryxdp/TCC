def conta_numero(num_recebido,matriz_recebida):
    matriz = []
    for i in matriz_recebida:
        linha = []
        for j in i:
            elemento = matriz_recebida.count(num_recebido)
            linha.append(elemento)
        matriz.append(linha)
    return(matriz)