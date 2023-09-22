def conta_frases(frases):
    v=len(str.split(frases,"!"))
    x=len(str.split(frases,"."))
    y=len(str.split(frases,"..."))
    z=len(str.split(frases,"?"))
    if y+x>=10:
        return v-1+x-1+y-7+z-1
    elif y+x>=7:
        return v-1+x-1+y-4+z-1
    elif y+x>=4:
        return v-1+x-1+y-4+z-1
    else:
        return v-1+x-1+y-1+z-1