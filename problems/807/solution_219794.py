def conta_frases(texto):
    frases=texto.replaceAll('...','!')
    frases=frases.replaceAll('?','!')
    frases=frases.replaceAll('.','!')
    
    print (frases)
    return len(frases)