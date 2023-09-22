def conta_numero(numero,matriz):
    ''' idéia: abrir um contador , e fazer ele andar pelas linhas da matriz
     e se enquanto ele anda algum elemento for igual ao numero,
     abro o contador e somo outro.'''
    matriz = []
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i] == numero:
    			contador = contador+1
            contador = contador+1
        contador = contador+1
    return contador