def posLetra(s,let,num):    
    cont=0
    n=0
    while n<len(s):
        if let==s[n]:
            cont+=1
        n+=1
    if cont==num:
        return n-1
    else:
        return -1