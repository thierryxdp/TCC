def conta_frases(frases):
    v=str.find(frases,"!")
    x=str.find(frases,".")
    z=str.find(frases,"?")
    
    return v-1+x-1+z-1