def conta_numero(num,matriz):
    qtd = 0 
    lista = []
    for i in matriz:
        for j in i:
            if j == numero:
                qtd += 1
        return qtd