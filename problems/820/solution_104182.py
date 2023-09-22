def posLetra(s,l,o):
    pos=[]
    for x in s:
        i=0
        if x=='l':
            pos.append(i)
        i=i+1
   	if o>len(pos):
        return -1
    else:
        return pos[o]