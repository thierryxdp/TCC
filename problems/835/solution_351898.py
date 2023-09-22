def melhor_volta(corrida):
    """retorna quem deu a melhor volta, qual o tempo e em qual volta.(list->tuple)"""
    melhorvolta=0
    resultado=()
    for i in range(len(corrida)):
        for j in range(len(corrida[i])):
            if corrida[i][j]>melhorvolta:
                melhorvolta=corrida[i][j]
                resultado=(i+1,melhorvolta,j+1)
    return resultado