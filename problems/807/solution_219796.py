def conta_frases(texto):
    frases=texto.replace('...','!')
    frases=frases.replace('?','!')
    frases=frases.replace('.','!')
    
    print (frases)
    return len(frases)