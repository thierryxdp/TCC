def conta_numero(numero, matriz):
   
    matriz2 = []
    for i in range (len(matriz)):
        for j in range (len(matriz[0])):
            if numero == matriz [i] [j]:
                matriz2.append(numero)
    return len(matriz2)