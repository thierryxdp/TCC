def eh_quadrada(matriz):
    ''''''
    novamat=[]
    for linha in matriz:
        novali=linha[:]
        novamat=novamat+[novali]
    if novamat<0:
        return novamat