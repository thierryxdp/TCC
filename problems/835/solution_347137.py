def melhor_volta(matriz):
    """ essa função ira retornar de quem foi a melhor volta, em qual tempo e qual volta
entrada -> list
saida -> tupla """
    vr = []
    for i in range(len(matriz)):
        min1 = min(matriz[i])
        vr = vr + list.append(vr,min1)
        minimo = min(vr)
    for k in range(len(matriz)):
        for m in range(len(matriz[k])):
            if minimo == matriz[k][m]:
                a = (k,minimo,m)
    return a