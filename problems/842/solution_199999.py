def pontos_por_time(lista1,lista2): # FAZER A IDENTIFICAÇÃO #
    nome1=lista1[0]
    nome2=lista2[0]
    cormengop1=lista1[2][0]
    cormengop2=lista2[2][1]
    flamintp1=lista1[2][1]
    flamintp2=lista2[2][0]
    if cormengop1>flamintp1:
        cormengop1=3
    if cormengop1<flamintp1:
        flamintp1=3 
    if flamintp2>cormengop2:
       flamintp2=3
    if cormengop2>flamintp2:
        cormengop2=3
    if cormengop1==flamintp1:
      cormengop1==1
    if cormengop1==flamintp1:
        flamintp1==1 
    if flamintp2==cormengop2:
      cormengop2=1
    if flamintp2==cormengop2:
        flamintp2==1
    pontos1= (cormengop1) + (cormengop2)
    pontos2= (flamintp1) + (flamintp2) 
    
    return {nome1:pontos1,nome2:pontos2}