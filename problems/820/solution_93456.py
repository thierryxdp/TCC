def posLetra(x,y,z):
    v=0
    h=0
    if x.count(y)<z:
        return -1
    else:
        while h<z:
            if x[v]==y:
                h=h+1
            v=v+1
        return v-1