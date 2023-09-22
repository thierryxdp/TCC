def melhor_volta(matriz):
    '''Recebe uma matriz em forma de lista e retorna em tupla 
    o menor tempo, o corredor que fê-la e a volta'''
    jogad_num=[]
    jogad=1
    temp=[]
    rod=[]
    for i in matriz:
        list.append(jogad_num,jogad)
        list.append(temp,min(i))
        list.append(rod,list.index(i,min(i)))
        jogad=jogad+1
    temp_min=min(temp)
    rod_t=rod[list.index(i,min(i))+int(1)]
    jogad_ven=jogad_num[list.index(i,min(i))+int(1)]
    return (jogad_ven,temp_min,rod_t)