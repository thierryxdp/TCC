def melhor_volta(matriz):

    melhor_volta = 0
    for linha in matriz:
        for coluna in linha:
            if coluna > melhor_volta:
                melhor_volta = coluna
                corredor = linha
    
    return (melhor_volta,matriz[corredor])