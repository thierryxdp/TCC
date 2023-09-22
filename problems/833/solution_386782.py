def conta_numero(numero,matriz):
    contagem=0
    for elementos in matriz[0][0]:
    	if (elementos==numero):
            contagem+=1
    return contagem