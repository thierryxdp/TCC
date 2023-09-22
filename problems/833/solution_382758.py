def conta_numero(numero,matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    qtd_n = 0
    
    for i in range(linhas):
        for j in range(colunas):
        	if str(numero) in str(matriz[i]):
        		qtd_n += str.count(str(matriz),str(numero))
    return qtd_n