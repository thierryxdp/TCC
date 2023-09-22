#
#
#
#
def posLetra(string,letra,numero):
    i=0    
    c=str.count(string,letra)
    if c < numero:
        return -1
    while i < len(string):
        p=0
        p=str.find(string,letra)
        i=i+1
    return p