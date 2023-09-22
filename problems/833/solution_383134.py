def conta_numero(numero,matriz):
    ''' idéia: abrir um contador , e fazer ele andar pelas linhas da matriz
     e se enquanto ele anda algum elemento for igual ao numero,
     abro o contador e somo outro.'''
    contador = 0
    for contador in range(len(matriz)):
        for j in range(len(matriz[i])):
            if contador == numero:
                contador = contador +1
            return contador