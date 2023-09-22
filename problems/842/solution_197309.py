def pontos_por_time2(info1,info2):
    '''Dados os placares dos jogos da ida e volta, retornará o número de
    pontos que cada time somou. (lista, lista=>dic)'''
    
    dadosfinais = {'cormengo','flaminthians'}

    if info1[0] > info1[1]:
        dadosfinais[0] += 3

    elif info1[0] < info1[1]:
        dadosfinais[1] += 3

    elif info1[0] == info1[1]:
        dadofinais[1]+= 1
        dadofinais[0]+= 1
        
    elif info2[0] > info2[1]:
        dadosfinais[0] += 3

    elif info2[0] < info2[1]:
        dadosfinais[1] += 3

    elif info2[0] == info2[1]:
        dadofinais[1]+= 1
        dadofinais[0]+= 1

    return dadosfinais