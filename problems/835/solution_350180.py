def melhor_volta(matriz):
    '''Recebe uma matriz em forma de lista e retorna em tupla 
    o menor tempo, o corredor que fê-la e a volta'''
    rod=1
    rod_acu=[]
    mini_p_rod=[]
    jogad=[]
    for i in matriz:
        list.append(jogad,i)
        list.append(mini_p_rod,min(i))
        list.append(rod_acu,rod)
        rod=rod+1
    return mini_p_rod,rod_acu,jogad