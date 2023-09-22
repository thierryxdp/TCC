def conta_numero(numero, matriz):
    lin = len(matriz)
    qtd = 0
    if lin == 0:
        qtd = 0 
    col =len(matriz[0])
    for i in range(0,lin):
    	for c in range(0,col):
			if numero == matriz[i][c]:
               	qtd +=1
                       
    return qtd