def melhor_volta(matriz):
    '''Recebe uma matriz em forma de lista e retorna em tupla 
    o menor tempo, o corredor que fê-la e a volta'''
    rod=1
    mini_p_rod=[]
    for i in matriz:
        mini_p_rod=mini_p_rod+list(min(i))
        rod=rod+1
    return