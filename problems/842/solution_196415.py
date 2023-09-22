def pontos_por_time(i):
    p=i[0]
    s=i[1]
    p1=p[2]
    s1=s[2]
    if p1[0]>p1[1] :
        p1[0]=3
        p1[1]=0
    elif p1[0]<p1[1]:
        p1[0]=0
        p1[1]=3
    else:
        p1[0]=1
        p1[1]=1
    if s1[0]>s1[1]:
        s1[0]=3
        s1[1]=0   
    elif s1[0]<s1[1]:
        s1[0]=0
        s1[1]=3
    else:
        p1[0]=1
        p1[1]=1
    if p1[0]>p1[1]:
        return {(p[0]):p1[0]+s1[1],(p[1]):p1[1]+s1[0]}
    elif p1[0]<p1[1]:
        return {(p[1]):p1[1]+s1[0],(p[0]):p1[0]+s1[1]}
    else:        
        return {(p[0]):p1[0]+s1[1],(p[1]):p1[1]+s1[0]}