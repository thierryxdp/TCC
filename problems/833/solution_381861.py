def conta_numero (numero, matriz):
    '''Retorna a quantidade de vezes que o número inserido aparece dentro da matriz inserida;
    int, list -> int'''
    contador = 0 
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                contador += 1
            else: 
                pass 
    return contador