def melhor_volta(corredores):
    melhor = (0, 0, corredores[0][0])

    for corredor in corredores:
        min_volta = min(corredor)
        if min_volta < melhor[2]:
            melhor = (corredores.index(corredor), corredor.index(min_volta), min_volta)
    
    return melhor