def melhor_volta(matriz):
    menor = matriz[0][0]
    corredor = 0
    for linha in matriz:
        for aij in linha:
            if aij < menor:
                volta = linha.index(aij) + 1               
                menor = aij
                corredor = matriz.index(linha) + 1
    return corredor,menor,volta