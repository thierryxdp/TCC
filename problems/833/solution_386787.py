def conta_numero(numero,matriz):
    contagem=0
    j=0
    for elementos in matriz:
		if elementos in matriz[0]:
            contagem+=1
        if elementos in matriz[0][1]:
            contagem+=1
    return contagem