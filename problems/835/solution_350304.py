def melhor_volta(matriz):
    '''informa qual corredor teve a volta mais rapida, o tempo,
       e qual foi a volta
       list -> tuple'''
    
    menores_tempos=[]
    a=0
    
    for i in matriz:
        list.append(menores_tempos, min(i))
    
    while a<6:
        if menores_tempos[a]==min(menores_tempos):
            return (a+1, min(menores_tempos))
        else:
            a+=1