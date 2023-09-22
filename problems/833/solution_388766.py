def conta_numero(numero, matriz):
    i=0
    vezes=[]
    while i<=len(matriz):
        vezes.append(matriz[i].count(numero))
        i=i+1
    return vezes