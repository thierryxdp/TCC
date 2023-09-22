def con_numero(numero,matriz):
    qtd = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            qtd += str.count(str(matriz),str(numero))
    return qtd