def conta_numero(numero,matriz):
    ''' idéia: abrir um contador , e fazer ele andar pelas linhas da matriz
     e se enquanto ele anda algum elemento for igual ao numero,
     abro o contador e somo outro.'''
    contador = 0
    for i in range(len(matriz)):
        qtd = []
        for j in range(len(matriz[i])):
            if matriz[i] == numero:
                qtd = qtd+1
    return len(qtd)