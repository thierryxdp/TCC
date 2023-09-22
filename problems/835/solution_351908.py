def melhor_volta(corrida):
    """retorna quem deu a melhor volta, qual o tempo e em qual volta.(list->tuple)"""
    resultado=()
    for i in range(6):
        melhorvolta=min(corrida[0])
        for j in range(10):
            if corrida[i][j]<melhorvolta:
                melhorvolta=corrida[i][j]
                resultado=(i+1,melhorvolta,j+1)
            else:
                resultado=1,melhorvolta
                
    return resultado