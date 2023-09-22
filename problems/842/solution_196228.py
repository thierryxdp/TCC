def pontos_por_time(i):
    p=i[0]
    s=i[1]
    p1=p[2]
    s1=s[2]
    if p1[0]>p1[1] :
        p[0]==3
        p[1]==0
    elif p1[0]<p1[1]:
        p[0]==0
        p[1]==3
    else:
        p[0]==1
        p[1]==1
    if s1[0]>s1[1]:
        s[0]==3
        s[1]==0   
    elif s1[0]<s1[1]:
        s[0]==0
        s[1]==3
    else:
        p[0]==1
        p[1]==1
    if p[0]>p[1]:
        return {(p[0]):p[0],(p[1]):p[1]}
    elif p[0]<p[1]:
        return {(p[1]):p[1],(p[2]):p[2]}
    else:        
    return {(p[0]):p[o],(p[1]):p[1]} or {(p[1]):p[1],(p[0]):p[0]}
    if s[0]>s[1]:
        return {(s[0]):s[0],(s[1]):s[1]}
    elif s[0]<s[1]:
        return {(s[1]):s[1],(s[2]):s[2]}
    else:        
    return {(s[0]):s[o],(s[1]):s[1]} or {(s[1]):s[1],(s[0]):s[0]}