def melhor_volta(m:list):
    t=m[0][0]
    p=0 #piloto
    v=0#volta
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j]<t:
                t=m[i][j]
                p=(i+1)
                v=(j+1)
	return (p,t,v)