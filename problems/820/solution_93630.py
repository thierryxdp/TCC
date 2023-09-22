def posLetra(string,letra,num):
    i=0
    x=str.count(string,letra)
    if x!=num:
        return -1
    while x==num:
        y=str.index(string,letra)
        y=y+1
        
    i=i+1
    return y