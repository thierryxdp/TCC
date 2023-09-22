def posLetra(string,letra,num):
    i=0
    x=str.count(string,letra)
    if x!=num:
        return -1
    while x==num:
        y=string[i]+1
    i=i+1
    return y