def posLetra(s,l,o):
    pos=[]
    i=0
    for x in s:
        if x==l:
            pos.append(i)
        i=i+1
   	
    if o>len(pos):
        return -1
    else:
        return pos[o-1]