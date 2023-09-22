def melhor_volta(matriz): #Entrada: Matriz (list)
    matriz = min(matriz)
    melhorestemposdomelhorcorredor = min(matriz)
    menortempo = min(melhorestemposdomelhorcorredor)

    corredor = matriz.index(melhorestemposdomelhorcorredor) + 1

    melhorvolta = melhorestemposdomelhorcorredor.index(menortempo) + 1

    return (corredor, menortempo, melhorvolta)