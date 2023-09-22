def melhor_volta(matriz):
    '''informa qual corredor teve a volta mais rapida, o tempo,
       e qual foi a volta
       list -> tuple'''
    
    menores_tempos=[]
    a=0
    tupla=()
    volta=0
    menor=0
    corredor=0
    
    for i in matriz:
        list.append(menores_tempos, min(i))
    menor= min(menores_tempos)
    
    while a<6:
        if menores_tempos[a]==menor:
            corredor=a+1
        a+=1
    
    for i in matriz:
        if menor in i:
            volta=list.index(i, menor)
            
    return (corredor, menor, volta)