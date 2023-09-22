def melhor_volta(tempos):
    t=[]
    i=0
    for a in tempos:
        for j in a:
        	t.append(j)
    while min(t) not in tempos[i]:
        i+=1
    melhor=min(t)
    corredor=i+1
    volta=tempos[i].index(min(t))
    	
    return (corrredor,melhor,volta)