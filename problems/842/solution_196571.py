def pontos_por_time ( lista ) :
i1 = l1[0] #['a','b',[x,x]]
    p1 = i1[2] #[x,x]
    i2 = l1[1] #['b','a',[y,y]]
    p2 = i2[2] #[y,y]
    pta = 0
    ptb = 0
    if p1[0] > p1[1]:
        pta = pta + 3
    elif p1[0] == p1[1]:
        ptb = ptb + 1
        pta = pta + 1
    else:
        ptb = ptb + 3
        
    if p2[0] > p2[1]:
        ptb = ptb + 3
    elif p2[0] == p2[1]:
        ptb = ptb + 1
        pta = pta + 1
    else:
        pta = pta + 3
        
    dic = {i1[0]:pta, i2[0]:ptb}   
    return dic