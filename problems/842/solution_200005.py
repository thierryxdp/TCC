def pontos_por_time(lista): # FAZER A IDENTIFICAÇÃO #
    nome1=lista[0][0]
    nome2=lista[0][1]
    cormengo_p1=lista[0][2][0]
    cormengo_p2=lista[1][2][1]
    flamint_p1=lista[0][2][1]
    flamint_p2=lista[1][2][0]
    if cormengo_p1>flamint_p1:
        cormengo_p1=3
    if cormengo_p1<flamint_p1:
        flamint_p1=3 
    if flamint_p2>cormengo_p2:
        flamint_p2=3
    if cormengo_p2>flamint_p2:
        cormengo_p2=3
    if cormengo_p1==flamint_p1:
        cormengo_p1==1
    if cormengo_p1==flamint_p1:
        flamint_p1==1 
    if flamint_p2==cormengo_p2:
        cormengo_p2=1
    if flamint_p2==cormengo_p2:
        flamint_p2==1
    pontos1= (cormengo_p1) + (cormengo_p2)
    pontos2= (flamint_p1) + (flamint_p2) 
    
    return {nome1:pontos1,nome2:pontos2}