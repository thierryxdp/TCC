def conta_numero(numero,matriz):
    qnt = 0
    j = 0
    k = 0
    for i in matriz[j]:
        qnt = qnt + list.count(matriz[j][k], numero)
    	j = j+1
    	k = k+1
    return qnt