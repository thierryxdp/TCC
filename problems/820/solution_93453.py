def posLetra(x,y,z):
    v=0
    h=0
    while h<z:
        if x[v]==y:
            h=h+1
        v=v+1
    return v-1