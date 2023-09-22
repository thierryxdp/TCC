def melhor_volta(ls):
    menores_voltas = []
    melhor_volta = 0
    for voltas in ls:
        menores_voltas.append(min(voltas))
        if min(menores_voltas) in voltas:
            melhor_volta = voltas.index(min(menores_voltas))
            melhor_corredor = ls.index(voltas)
    return (melhor_corredor+1 , min(menores_voltas) , melhor_volta+1)