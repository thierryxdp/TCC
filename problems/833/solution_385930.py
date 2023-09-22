def conta_numero(num,matriz):
    a=0
    for x in matriz :
        qtd=0
        for c in x:
            if c== num:
                qtd = qtd + 1
                return  qtd 
            else:
                return a