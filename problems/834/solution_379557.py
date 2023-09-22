def media_matriz ( matriz ) :
    media = 0
    elementos = 0
    for linha in matriz :
        for elemento in linha :
            elementos += 1
            media += elemento
    media = media / elementos
    media = round ( media , 2 ) 
    return media