def conta_numero(numero,matriz):
    qtd_num=0
    for i in matriz:
        for j in i:
            if int(numero)== int(j):
                qtd_num=qtd_num+1
    return qtd_num