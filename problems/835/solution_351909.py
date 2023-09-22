def melhor_volta(corrida):
    """retorna quem deu a melhor volta, qual o tempo e em qual volta.(list->tuple)"""
    resultado=()
    for i in range(len(corrida)):
        for j in range(corrida[i]):
            if corrida[i][j]<melhorvolta:
                melhorvolta=corrida[i][j]
                resultado=(i+1,melhorvolta,j+1)
            else:
                resultado=1,melhorvolta
                
    return resultado