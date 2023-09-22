def conta_numero(numero, matriz):

#retorna quantas vezes um número dado apararece em uma matriz dada    
    
    lista = []

    for l in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[l][c] == numero:
                lista.append(numero)

    return len(lista)