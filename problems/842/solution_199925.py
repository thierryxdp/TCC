def pontos_por_time(lista1): # FAZER A IDENTIFICAÇÃO #
    nome1=str(lista1[0])
    nome2=str(lista1[1])
    nome1_p1=lista1[0][2][0]
    nome1_p2=lista1[0][2][1]
    nome2_p1=lista1[1][2][1]
    nome2_p2=lista1[1][2][0]
    if nome1_p1>nome2_p1:
        nome1_p1=3
    if nome1_p1<nome2_p1:
        nome2_p1=3 
    if nome2_p2>nome1_p2:
        nome2_p2=3
    if nome1_p2>nome2_p2:
        nome1_p2=3
    if nome1_p1==nome2_p1:
        nome1_p1==1
    if nome1_p1==nome2_p1:
        nome2_p1==1 
    if nome2_p2==nome1_p2:
        nome1_p2=1
    if nome2_p2==nome1_p2:
        nome2_p2==1
    pontos1= (nome1_p1) + (nome1_p2)
    pontos2= (nome2_p1) + (nome2_p2) 
    return {nome1:pontos1,nome2:pontos2}