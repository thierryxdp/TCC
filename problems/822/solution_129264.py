def repetidos(l):
    x=1
    y=0
    while x<len(l):
        if l[x]==l[x-1]:
            y+=1
        x+=1
    return y