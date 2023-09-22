def melhor_volta(corrida):
    """retorna quem deu a melhor volta, qual o tempo e em qual volta.(list->tuple)"""
    resultado=()
    for i in range(len(corrida)):
        melhorvolta=min(corrida[i])
        for j in range(len(corrida[i])):
            if corrida[i][j]<melhorvolta:
                melhorvolta=corrida[i][j]
                resultado=(i+1,melhorvolta,j+1)
    return resultado