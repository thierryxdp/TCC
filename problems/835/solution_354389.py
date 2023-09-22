def melhor_volta(ls):
    '''função que dada uma matriz 6x10 com os tempos em segundos de cada
    corredor de kart, retorna uma tupla informando de quem foi a melhor
    volta, o tempo e em que volta
    list->tuple'''
    
    menores_voltas=[]
    melhorvolta=0
    
    for voltas in ls:
        menores_voltas.append(min(voltas))
        if min(menores_voltas) in voltas:
            melhorvolta=voltas.index(min(menores_voltas))
            melhor_corredor=ls.index(voltas)
            
    return (melhor_corredor+1,min(menores_voltas),melhorvolta+1)