def conta_frases(texto):
    frases=texto.replace('...','!')
    frases=frases.replace('?','!')
    frases=frases.replace('.','!')
    
    frases=frases.split('!')
    return (len(frases))-1