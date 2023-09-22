def conta_frases(frases):
    v=str.split(frases,"!")
    x=str.split(frases,".")
    return len(v-1)+len(x-1)