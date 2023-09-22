def melhor_volta(matriz):
    '''função que identifica de quem foi a melhor volta, com qual tempo e
    	que volta. lista->tupla'''
    tempo=matriz[0][0]
    for i in range(6):
        if min(matriz[i])<=tempo:
            tempo=min(matriz[i])
            corredor=i+1
            volta=list.index(matriz[i],tempo)
    return (corredor,tempo,volta)