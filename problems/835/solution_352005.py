def melhor_volta(ls):
    """Essa função serve para identificar (dada a matriz (ls)) qual
    corredor teve o melhor tempo, qual foi este tempo, e em qual volta.
    list->tuple"""
    menores_voltas = []
    melhor_volta = 0
    for voltas in ls:
        menores_voltas.append(min(voltas))
        if min(menores_voltas) in voltas:
            melhor_volta = voltas.index(min(menores_voltas))
            melhor_corredor = ls.index(voltas)
    return (melhor_corredor+1 , min(menores_voltas) , melhor_volta+1)

#Para facilitar os testes, eu reduzi a quantidade de voltas, mas o programa ainda é válido para a matriz 6x10

#melhor_volta([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]) == (1, 1, 1)
#melhor_volta([[13,14,15],[4,5,6],[7,8,9],[10,11,12],[3,2,56],[16,17,18]]) == (5, 2, 2)
#melhor_volta([[13,14,15,90,91],[4,5,6,67,89],[7,8,9,92,93],[10,11,12,94,95],[3,2,56,96,97],[16,17,1,98,99]]) == (6, 1, 3)