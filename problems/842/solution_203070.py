#Start your python function here
d={ls[0[0]]:0,ls[0[1]]:0}
def pontos_por_times(ls):
    if ls[0[2[0]]]>ls[0[2[1]]]:
        d[0]+=3
    elif ls[0[2[0]]]<ls[0[2[1]]]:
        d[1]+=3  
    elif ls[0[2[0]]]==ls[0[2[1]]]:
        d[0,1]+=1    
    if ls[1[2[0]]]>ls[1[2[1]]]:
        d[1]+=3 
    elif ls[1[2[0]]]>ls[1[2[1]]]:
        d[0]+=3  
    elif ls[1[2[0]]]==ls[1[2[1]]]:
        d[0,1]+=1 
    return d