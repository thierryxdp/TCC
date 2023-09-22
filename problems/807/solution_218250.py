def conta_frases(frases):
    v=len(str.split(frases,"!"))
    x=len(str.split(frases,"."))
    y=len(str.split(frases,"..."))
    y1=''.join(y)
    z=len(str.split(frases,"?"))
    return v-1+x-1+y1-1+z-1