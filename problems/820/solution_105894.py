def posLetra(s,x,n):
    k = -1
    g = 0
    for i in range(len(s)):
        if(string[i]==x):
            g=g +1
        if(g==n):
            k == i
            break
    return k