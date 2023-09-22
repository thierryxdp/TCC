def conta_numero(num,matriz):
    qtd=0
    for i in matriz:
        for j in range(len(matriz[0])):
            if i[j]==num:
                qtd+=1
    return qtd