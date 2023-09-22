def conta_numero(numero,matriz):
    count=0
    for i in matriz:
        for j in i:
            if j == numero:
            count= count+1
    return count