def melhor_volta(m):
    a=0
    b=0
    c=0
    tempo=[]
    
    for i in range(len(m)):
        for j in range(len(m[0])):
            list.append(tempo,min(m[i]))
            b=min(tempo)
            if b in m[i]:
                a=i+1
                if b in a:
                    c=m[i]
            
    return a,b,c