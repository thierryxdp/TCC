def melhor_volta(m):

    corredor=0
    
    for linha in m:
        for posicao in linha:
            if posicao==min(posicao):
                corredor+=1
    return corredor