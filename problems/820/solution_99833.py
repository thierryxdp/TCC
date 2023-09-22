#
#
#
#
def posLetra(string,letra,numero):
    i=0
    pos=0
    c=str.count(string,letra)
    if c < numero:
        return -1
    while i < len(string):        
        p=str.find(string,letra)
        pos=pos+p
        l=str.replace(pos,p)
        i=i+1
    return l