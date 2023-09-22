#
#
#
#
def posLetra(string,letra,numero):
    i=0
    c=0
    while c < numero:
        if string[i] == letra:
            c=c+1
        i=i+1
    return i-1