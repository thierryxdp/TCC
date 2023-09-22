def conta_frases(frases):
    v=str.split(frases,"!")
    x=str.split(frases,".")
    y=str.split(frases,"...")
    z=str.split(frases,"?")
    if y+x>=8:
        return v-1+x-1+y-7+z-1
    elif y+x>=7:
        return v-1+x-1+y-4+z-1
    else:
        return v-1+x-1+y-1+z-1