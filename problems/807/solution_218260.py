def conta_frases(frases):
    v=str.split(frases,"!"))
    x=str.split(frases,"."))
    y=str.split(frases,"..."))
    y1=''.join(y)
    z=str.split(frases,"?"))
    return len(v)-1+len(x)-1+len(y1)-1+len(z)-1