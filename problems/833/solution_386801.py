def conta_numero(numero,matriz):
    contagem=0
    for elementos in matriz[:-1]:
    	if (elementos==numero):
            contagem+=1
    return contagem