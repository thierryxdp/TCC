def melhor_volta(m:list):
    t=m[0][0]
    p=0 #piloto
    v=0#volta
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j]<t:
                t=m[i][j]
                p=(i)
                v=(j)
	return (p,t,v)