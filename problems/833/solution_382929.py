def conta_numero(numero,matriz):
    ''' idéia: abrir um contador , e fazer ele andar pelas linhas da matriz
     e se enquanto ele anda algum elemento for igual ao numero,
     abro o contador e somo outro.'''
    i = 0
    for i in range(len(matriz)):
        if matriz[i] == numero:
        i = i+1
    return i