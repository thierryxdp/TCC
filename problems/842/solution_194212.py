def pontos_por_time(lista1,lista2):
    '''retorna o numero de pontos de um time na fase do campeonato'''
    
    gol1=lista1[2][0]+lista2[2][1]
    gol2=lista1[2][1]+lista2[2][0]
    
    pontogeral={}
    if gol1<gol2:
        return pontogeral+(gol2*3)
   	if gol1>gol2:
        return pontogeral+(gol1*3)
    if:
        return pontogeral+(gol1)