def conta_numero(numero,matriz):
    quantidade = 0
    for linhas in matriz:
        for colunas in linhas:
            if colunas == numero:
                quantidade += 1
    return quantidade