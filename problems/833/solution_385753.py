def conta_numero(numero,matriz):
    """conta a frequencia do numero dado como entrada
    na matriz; int,list[list[int]]->int"""
    freq=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                freq+=1
    return freq