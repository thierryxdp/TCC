def conta_frases(frases):
    v=len(str.split(frases,"!"))
    x=len(str.split(frases,"."))
    y=len(str.split(frases,"..."))
    z=len(str.split(frases,"?"))
    if x>=8:
        return v-1+x-1+y-7+z-1
    elif y+x>=7:
        return v-1+x-1+y-4+z-1
    elif x+y>=4 and v==0 and z==0:
        return v-1+x-1+y-3+z-1
    else:
        return v-1+x-1+y-1+z-1