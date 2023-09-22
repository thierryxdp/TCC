def conta_numero(numero,matriz):
    M=[]
	contador=0
    linhas= len(matriz)
    colunas= len(matriz[0])
    for i in range(linhas):
        for j in range (colunas):
            if 9 == numero:
            	contador = contador + 1
    return contador