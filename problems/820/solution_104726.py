def posLetra (texto,letra,n):
    total=texto.count(letra)
    i=0
    qtd_ocorrencias=0
    if n<=total:
        while qtd_ocorrencias<n:
            if texto[i] in letra:
                qtd_ocorrencias = qtd_ocorrencias + 1
            i = i+1
    	return i-1
    else: 
    	return -1