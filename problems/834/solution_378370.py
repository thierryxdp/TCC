def media_matriz(matriz):
    j = 0
    soma = 0 
    elementos = 0
    i = 0
    while i < len(matriz):
        c = sum(matriz[j])
        soma = soma + c
        d = len (matriz[j])
        j = j + 1
        elementos = elementos + d
    	return soma/elementos