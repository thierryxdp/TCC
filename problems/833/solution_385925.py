def conta_numero(matriz,num):
    ocorrencias = []
    for x in matriz :
        qtd=0
        for c in x:
            if c== num:
                qtd = qtd + 1
                return  qtd