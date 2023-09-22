def melhor_volta(tempos):
    t=[]
    i=0
    for i in tempos:
    	for j in i:
            t.append(i)
    while min(t) not in tempos[i]:
        i+=1
    melhor=min(t)
    corredor=i+1
    volta=matriz[i].index(melhor)+1
    	
    return (corrredor,melhor,volta)