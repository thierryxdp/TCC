def melhor_volta(m):
    
    len(m)==6
    len(m)[0]==10
    corredor=0
    
    for linha in m:
        for posicao in linha:
            if posicao in min(posicao):
                corredor+=1
    return corredor