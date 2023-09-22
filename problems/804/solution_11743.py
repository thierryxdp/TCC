def T():
    a = T[0]%2
    b = T[1]%2
    c = T[2]%2
    d = T[3]%2
    if a==b==c==d==0:
        return T[0],T[1],T[2],T[3]
    if a==b==c==0:
        return T[0],T[1],T[2] 
    if b==c==d==0: 
        return T[1],T[2],T[3] 
    if a==c==d==0: 
        return T[0],T[2],T[3] 
    if a==b==d==0: 
        return T[0],T[1],T[3] 
    if a==b==0: 
        return T[0],T[1] 
    if b==c==0: 
        return T[1],T[2] 
    if c==d==0: 
        return T[2],T[3] 
    if a==c==0: 
        return T[0],T[2] 
    if a==d==0: 
        return T[0],T[3] 
    if b==d==0: 
        return T[1],T[3]  
    if a==0: 
        return T[0] 
    if b==0: 
        return T[1] 
    if c==0: 
        return T[2] 
    if d==0: 
        return T[3]