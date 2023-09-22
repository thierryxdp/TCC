def pontos_por_time(lista1,lista2):
    pontosA=[]
    pontosB=[]
    if lista1[3][0]>lista1[3][1]:
        pontosA=pontosA+3
   	if lista1[3][0]==lista1[3][1]:
        pontosA=pontosA+1
        pontosB=pontosB+1
    if lista1[3][0]<lista1[3][1]:
        pontosB=pontosB+3
    if lista2[3][0]<lista2[3][1]:
        pontosA=pontosA+3
   	if lista2[3][0]==lista2[3][1]:
        pontosA=pontosA+1
        pontosB=pontosB+1
    if lista2[3][0]>lista2[3][1]:
        pontosB=pontosB+3
        return pontosA