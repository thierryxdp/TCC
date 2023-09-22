def conta_frases(frases):
    i=0
    con=0
    while i<len(frases):
        if(frases[i] in "!?..."):
            con=con+1
            i=i+1
        else:
            i=i+1
    return con