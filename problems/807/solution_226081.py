def conta_frases(texto):
    frases = str.split(texto,"!","?")
    #frases = str.split(frases,". ","...")
    return len(frases)