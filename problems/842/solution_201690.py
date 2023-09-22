def pontos_por_time(lista1,lista2):
    tabela1={lista1[0]:6,lista1[1]:0}
    tabela2={lista1[0]:4,lista1[1]:1}
    tabela3={lista1[0]:3,lista1[1]:3}
    tabela4={lista1[0]:4,lista1[1]:1}
    tabela5={lista1[0]:2,lista1[1]:2}
    tabela6={lista1[0]:1,lista1[1]:4}
    tabela7={lista1[0]:3,lista1[1]:3}
    tabela8={lista1[0]:1,lista1[1]:4}
    tabela9={lista1[0]:0,lista1[1]:6}
    if lista1[2][0]>lista1[2][1] and lista2[2][0]>lista2[2][1]:
        return tabela1
    if lista1[2][0]>lista1[2][1] and lista2[2][0]==lista2[2][1]:
        return tabela2
    if lista1[2][0]>lista1[2][1] and lista2[2][0]<lista2[2][1]:
        return tabela3
    if lista1[2][0]==lista1[2][1] and lista2[2][0]>lista2[2][1]:
        return tabela4
    if lista1[2][0]==lista1[2][1] and lista2[2][0]==lista2[2][1]:
        return tabela5
    if lista1[2][0]==lista1[2][1] and lista2[2][0]<lista2[2][1]:
        return tabela6        
    if lista1[2][0]<lista1[2][1] and lista2[2][0]>lista2[2][1]:
        return tabela7
    if lista1[2][0]<lista1[2][1] and lista2[2][0]==lista2[2][1]:
        return tabela8
    if lista1[2][0]<lista1[2][1] and lista2[2][0]<lista2[2][1]:
        return tabela9
    else: 
        return 'n'