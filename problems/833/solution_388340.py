def conta_numero(num_recebido,matriz_recebida):
    matriz = []
    c = 0
    for i in matriz_recebida:
        linha = []
        for j in i:
            if num_recebido in matriz_recebida:
                c = c + 1
        return c