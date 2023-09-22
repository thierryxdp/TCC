def melhor_volta(m):
    tempos=[]
    
    for i in m:
        for j in i:
            tempos+=[j]
            
    menor_t = min(tempos)
    motorista = (tempos.index(menor_t))//10 + 1
    voltas = (tempos.index(menor_t))%10 + 1
    
    return motorista,menor_t,voltas