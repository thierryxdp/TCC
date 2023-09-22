def pontos_por_time(info):
    '''Dados os placares dos jogos da ida e volta, retornará o número de
    pontos que cada time somou. (lista=>lista)'''
    
    dadosfinais = [0 , 0]

    if info[0][2][0] > info[0][2][1]:
        dadosfinais[0] += 3

    elif info[0][2][0] < info[0][2][1]:
        dadosfinais[1] += 3

    elif info[0][2][0] == info[0][2][1]:
        dadosfinais[0] += 1
        dadosfinais[1] += 1

    elif info[1][2][0] > info[1][2][1]:
        dadosfinais[1]+=3

    elif info[1][2][0] < info[1][2][1]:
        dadosfinais[0]+=3

    elif info[1][2][0] == info[1][2][1]:
        dadosfinais[0] += 1
        dadosfinais[1] += 1

    return {info[0][0]:dadosfinais[0], info[0][1]:dadosfinais[1]}