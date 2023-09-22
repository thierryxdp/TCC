def melhor_volta(matriz):
    linha = 0 
    coluna = 0
    menor = 0.0
    
    for lista in matriz:
        lista = [float(i) for i in lista]
        for val in lista:
            if val <= menor:
                menor = val
            else:
                coluna+= 1
                continue
            coluna = 0
        linha+=1
    return linha, val