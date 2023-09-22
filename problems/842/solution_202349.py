def pontos_por_time(lista):
    ''' função que dada dois elementos e informa a quantidade gols em dois jogos dados dois times; a saída é um dicionário list->dici'''
    tab1={lista[0][0]:6, lista[1][0]:0}
    tab2={lista[0][0]:3, lista[1][0]:3}
    tab3={lista[0][0]:0, lista[1][0]:6}
    tab4={lista[0][0]:4, lista[1][0]:1}
    tab5={lista[0][0]:1, lista[1][0]:4}
    tab6={lista[0][0]:2, lista[1][0]:2}
    if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
		return tab1
    if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
        return tab2
    if lista[0][2][0]<lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
        return tab2
    if lista[0][2][0]<lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
        return tab3
    if lista[0][2][0]>lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
        return tab4
    if lista[0][2][0]==lista[0][2][1] and lista[1][2][0]<lista[1][2][1]:
        return tab4
    if lista[0][2][0]<lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
        return tab5
    if lista[0][2][0]==lista[0][2][1] and lista[1][2][0]>lista[1][2][1]:
        return tab5
    if lista[0][2][0]==lista[0][2][1] and lista[1][2][0]==lista[1][2][1]:
        return tab6