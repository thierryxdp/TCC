def conta_numero(numero,matriz):
    qtd=0
    c=0
    k=0
    i=0
    j=0
    if len(matriz) == 1:
        while i<len(matriz):
            if numero == matriz[i][c]:
                i=i+1
                c=c+1
                qtd=qtd+1
        return qtd
    else:
        while j<len(matriz):
            if numero == matriz[j][k]:
                j=j+1
                k=k+1
                qtd=qtd+1
        return qtd