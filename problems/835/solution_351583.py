def melhor_volta(matriz):
    linha = 0
    coluna = 0
    menor = 0
    for lista in matriz:
        for i in lista:
        lista = i
        for valor in lista:
            if valor <= menor:
                menor = valor
            else:
                coluna+=1
        linha+=1
    return(linha, coluna)