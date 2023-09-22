def melhor_volta(matriz):
    '''funçao  que verifica quem fez  a  melhor
    volta, com que tempo e em que volta'''
    'list--> tuple'
    lista_tempos = list()
    lista_voltas = list()

    for voltas in range(6):
        for tempos in range(10):
            if matriz[voltas][tempos] == min(matriz[voltas]):
                   lista_tempos.append(tempos)
    for voltas in range(6)  :
        lista_voltas.append(matriz[voltas][lista_tempos[voltas]])
        cada_volta = lista_voltas.index(min(lista_voltas))
        melhor_volta = min(lista_voltas)
        corredores = matriz[melhor_volta].index(melhor_volta) + 1 
    return corredores