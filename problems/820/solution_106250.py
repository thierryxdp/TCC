def posLetra(string,l,num):
    m=0
    for i,e in enumerate(string):
        if e==l:
            m+=1
        if m==num:
            return i
    return -1