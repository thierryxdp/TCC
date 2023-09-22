def melhor_volta(m):
    """Funcao que recebe uma matriz 6x10 com os tempos em segundos dos
    corredores em cada volta. Retorna quem fez a melhor volta, o tempo 
    dessa volta e qual a volta. Obs: só deverá ter tempos diferentes;
    list(list) -> tuple"""
    
    corredores = len(m)
    voltas = len(m[0])
    melhores = []

    for i in range(corredores):
        tempos = []
        for j in range(voltas):
            list.append(tempos,m[i][j])
        melhores = melhores + [min(tempos)] 
        
    melhor_volta = min(melhores)
    
    melhor_corredor = list.index(melhores,melhor_volta) + 1
    
    indice_corredor = list.index(melhores,melhor_volta) 
    melhor_volta_corredor = list.index(m[indice_corredor],melhor_volta) + 1
    
    return melhor_corredor, melhor_volta, melhor_volta_corredor