def melhorvolta(ls):
    """função que recebe uma matriz 6x10 com os tempos em segundos dos 
    corredores de um kart, e retorna uma tupla de quem foi a melhor volta,
    o tempo e em que volta
    list->tuple"""
    
    menores_voltas = []
    melvolt= 0  

    for voltas in ls:     
        menores_voltas.append(min(voltas))         
        if min(menores_voltas) in voltas:             
            melvolt = voltas.index(min(menores_voltas))             
            melhor_corredor = ls.index(voltas)     
            
    return (melhor_corredor+1 , min(menores_voltas) , melvolt+1)