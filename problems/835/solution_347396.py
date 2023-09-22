def melhor_volta(m:list)->tuple:
    """"função que, dada uma matriz 6 por 10 com os tempos em segundos dos corredores em cada volta, retorna uma tupla
    informando de quem foi a melhor volta, com qual tempo e em que volta.
    
    parametros:
    list -> tuple
 	"""
    acumulador=[0,9999999,0]
    for i in range(6):
        for j in range(10):
            if m[i][j]<acumulador[1]:
                acumulador[1]=m[i][j]
                acumulador[0]=i+1
                acumulador[2]=j+1
    return tuple(acumulador)