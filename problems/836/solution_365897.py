def busca(nome,matriz):
    contador=[]
    for i in range(len(matriz)):
        if nome in matriz[i][2]:
            contador += matriz[i]
    return contador