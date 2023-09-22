def posLetra(string,letra,num):
    i=0
    L=letra
    x=str.count(string,letra)
    if x!=num:
        return -1
    while i<len(string):
        return str.index(string,L)