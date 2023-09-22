def conta_numero(numero,matriz):
    quantidade = 0
    lista_num = [numero]
    for i in range(0,len(matriz)):
        for j in range (0, len(matriz[0])):
        	if lista_num in matriz[i][j]:
            	quantidade +=1
    return quantidade