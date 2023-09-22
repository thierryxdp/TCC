#
#
#
#
def posLetra(string,letra,numero):
    i=0
    p=()
    c=str.count(string,letra)
    if c < numero:
        return -1
    while i < len(string):
        if string[i] == letra:
            p=p+str.append(p,i)
            i=i+1
    return p