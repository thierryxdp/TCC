def conta_numero(numero,matriz):
    matriz_seg=[]
    for x in range (len(matriz)):
        for y in range (len(matriz[0])):
            if numero == matriz [x] [y]:
                matriz_seg.append(numero)
    return len(matriz_seg)