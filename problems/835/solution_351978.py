def melhor_volta(corredores):
    melhor = (1, corredores[0][0], 1)

    for corredor in corredores:
        min_volta = min(corredor)
        if min_volta < melhor[1]:
            melhor = (corredores.index(corredor) + 1, min_volta, corredor.index(min_volta) + 1)
    
    return melhor