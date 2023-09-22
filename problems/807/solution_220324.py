def conta_frases(frases):
    frases1=frases.replace('.','&')
    frases2=frases1.replace('?','&')
    frases3=frases2.replace('!','&')
    frases4=len(frases3)
    return frases4