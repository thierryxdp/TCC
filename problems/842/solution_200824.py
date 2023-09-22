def pontos_por_time(lista)

	primFaseA=lista[0][1][0]
    primFaseB=lista[0][1][1]
    segFaseA=lista[1][1][0]
    segFaseB=lista[1][1][1]
    pontA=0
    pontB=0
    
    if primFaseA>primFaseB:
        pontA=pontA+3
    elif primFaseA==primFaseB:
        pontA=pontA+1
        pontB=pontB+1
    else:
        pontB=pontB+3
        
    if segFaseA>segFaseB:
        pontA=pontA+3
    elif segFaseA==segFaseB:
        pontA=pontA+1
        pontB=pontB+1
    else:
        pontB=pontB+3
        
    return {lista[0][0][0]: pontA}