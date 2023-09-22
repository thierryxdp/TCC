def pontos_por_time(lista1,lista2):
    pontostim1=0
    pontostim2=0
    time1=lista1[1][0]
    time2=lista1[1][1]
    lista1=lista[0]
    lista2=lista[1]
    desempenho = {time1:pontostim1, time2:pontostim2}
    if lista1[0][-1][0]>lista1[1][-1][1]:
           pontostim1 += 3
    if lista1[0][-1][0]==lista1[1][-1][1]:
           pontostim1 += 1
           pontostim2 += 1  
    if lista1[0][-1][0]<lista1[1][-1][1]:
           pontostim2 += 3
    if lista2[1][-1][0]>lista2[1][-1][1]:
           pontostim1 += 3
    if lista2[1][-1][0]==lista2[1][-1][1]:
           pontostim1 += 1
           pontostim2 += 1
    if lista2[1][-1][0]<lista2[1][-1][1]:
           pontostim2 += 3
    return desempenho