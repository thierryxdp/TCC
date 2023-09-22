def pontos_por_time(lista):

	primFaseA=lista[0][2][0]
    primFaseB=lista[0][2][1]
    segFaseA=lista[1][2][1]
    segFaseB=lista[1][2][0]
    pontAjogo1=0
    pontBjogo1=0
    pontAjogo2=0
    pontBjogo2=0
    
    if primFaseA>primFaseB:
        pontAjogo1=pontAjogo1+3
    elif primFaseA==primFaseB:
        pontAjogo1=pontAjogo1+1
        pontBjogo1=pontBjogo1+1
    else:
        pontBjogo1=pontBjogo1+3
        
    if segFaseA>segFaseB:
        pontAjogo2=pontAjogo2+3
    elif segFaseA==segFaseB:
        pontAjogo2=pontAjogo2+1
        pontBjogo2=pontBjogo2+1
    else:
        pontBjogo2=pontBjogo2+3
        
    return {lista[0][0]: pontAjogo1+pontAjogo2, lista[0][1]: pontBjogo1+pontBjogo2}