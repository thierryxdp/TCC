#
#
#
#
def posLetra(string, letra, numero):
    i=0
    pos=0
    while i<len(string):
        if pos<=numero:
            p=str.find(string,letra)
            i=i+1
            pos=pos+1
        return p