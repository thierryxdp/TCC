#Start your python function here
def pontos_por_times(ls):
    p1=0
    p2=0
    if ls[0[2[0]]]>ls[0[2[1]]]:
        p1=p1+3
    elif ls[0[2[0]]]<ls[0[2[1]]]:
        p2=p2+3  
    elif ls[0[2[0]]]==ls[0[2[1]]]:
        p1=p1+1
        p2=p2+1
    if ls[1[2[0]]]>ls[1[2[1]]]:
        p2=p2+3 
    elif ls[1[2[0]]]>ls[1[2[1]]]:
        p1=p1+3  
    elif ls[1[2[0]]]==ls[1[2[1]]]:
        p1=p1+1
        p2=p2+1 
    return {ls[0[0]]:p1,ls[0[1]]:p2}