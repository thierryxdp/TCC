def conta_numero(numero,matriz):
    qnt = 0
    j = 0
    
    for i in matriz[j]:
        c = list.count(matriz[j], numero)
        qnt = qnt + c 
        j = j+1
    return qnt