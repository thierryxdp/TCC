def conta_frases(frases):
    v=len(str.split(frases,"!"))
    x=len(str.split(frases,"."))
    y=len(str.split(frases,"..."))
    z=len(str.split(frases,"?"))
    if y+x>=3:
        return v+x+y-4+z