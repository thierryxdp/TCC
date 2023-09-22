def conta_frases(frases):
    i=0
    con=0
    while i<len(frases)-2:
        if(frases[i] in "!?"):
            con=con+1
            i=i+1
        elif(frases[i]=="." and frases[i+2]=="."):
            i=i+3
            con=con+1
        elif(frases[i]=="." and frases[i+2]!="."):
            i=i+1
            con=con+1
        else:
            i=i+1
        if(frases[len(frases) in ".!?"]:
           con=con+1
    return con