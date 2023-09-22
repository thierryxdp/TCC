def conta_numero(numero,matriz):
    contagem=[]
    j=0
    for elementos in matriz:
		if elementos in matriz[0]:
            contagem=contagem.append(elementos)
        if elementos in matriz[1][0]:
            contagem=contagem.append(elementos)
    return contagem