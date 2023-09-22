def melhor_volta(tempos):
    '''retorna o piloto que conseguiu menor tempo numa volta,
    seu tempo e sua volta
    list(list) -> tuple'''
    
    x=[]
    for pil in range(len(tempos)):
        i=0
        for volta in range(len(tempos[i])):
            list.append(x,tempos[pil][i])
            if tempos[pil][i] == min(x):
                y=(pil+1,tempos[pil][i],i+1)
            i+=1
    return y