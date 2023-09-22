def conta_frases(frases):
    v=len(str.split(frases,"!"))
    x=len(str.split(frases,".",1))
    y=len(str.split(frases,"..."))
    z=len(str.split(frases,"?"))
    return v+x+y+z