def conta_numero(numero,matriz):
    qnt = 0
    j = 0
    i = 0
    while i < len(matriz):
        c = list.count(matriz[j], numero)
        qnt = qnt + c 
        j = j+ 1
        i = i + 1
    return qnt