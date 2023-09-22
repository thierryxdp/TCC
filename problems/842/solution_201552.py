[['cormengo1','flaminthians',[1,0]],['flaminthians','cormengo',[2,2]]]


def pontos_por_time(lista1,lista2):
    pontostim1=0
    pontostime2=0
    desempenho = {lista1[1][0]:pontostim1,lista1[1][1]:pontostime2}
    if lista[0][-1][0]>lista[1][-1][1]:
        pontostim1 += 3
    elif lista[0][-1][0]==lista[1][-1][1]:
        pontostim1 += 1
        pontostim2 += 1  
    elif lista[0][-1][0]<lista[1][-1][1]:
        pontostim2 += 3
    elif lista[1][-1][0]>lista[1][-1][1]:
        pontostim1 += 3
    elif lista[1][-1][0]==lista[1][-1][1]:
        pontostim1 +=1
        pontostim2 += 1
    elif lista[1][-1][0]<lista[1][-1][1]:
        pontostim2 += 3
    return desempenho
   
    
    
    
    
    desempenho