def media_matriz(matriz):
	soma=0
	tam=0
	for linha in matriz:
    	soma+=sum(linha)
    	tam+=len(linha)
    x=soma/tam
    "%.2f" % x
    return x