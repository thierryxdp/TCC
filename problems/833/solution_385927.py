def conta_numero(num,matriz):
    ocorrencias = []
    for x in matriz :
        qtd=0
        for c in range(len(x)):
            if c== num:
                qtd = qtd + 1
                return  qtd