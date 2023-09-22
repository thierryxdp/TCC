def pontos_por_time(s):
    
    c=0
    d=0
    if(s[0][2][0]>s[0][2][1]):
        c=c+3
    elif(s[0][2][0]==s[0][2][1]):
        c=c+1
        d=d+1
    else:
        d=d+3
        
    if(s[1][2][0]>s[1][2][1]):
        d=d+3
    elif(s[1][2][0]==s[1][2][1]):
        c=c+1
        d=d+1
    else:
        c=c+3
    
    dic={s[0][0]:c,s[0][1]:d}

    return dic