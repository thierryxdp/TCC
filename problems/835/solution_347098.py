def melhor_volta(tempos):
    t=[]
    i=0
    for a in tempos:
    	for j in a:
            t.append(a)
    while min(t) not in tempos[j]:
        i+=1
    melhor=min(t)
    corredor=i+1
    volta=tempos[i].index(melhor)+1
    	
    return (corrredor,melhor,volta)