def melhor_volta(corrida):
    """retorna quem deu a melhor volta, qual o tempo e em qual volta.(list->tuple)"""
    resultado=()
    for i in range(len(corrida)):
        for j in range(len(corrida[i])):
            if min(corrida[i])==corrida[i][j]:
                resultado[i]=i+1,corrida[i][j],j+1
                  
    return resultado