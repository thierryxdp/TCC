def conta_frases(frases):
    frases[-1]=0
    frases1=frases.replace('.','&')
    frases2=frases1.replace('?','&')
    frases3=frases2.replace('!','&')
    frases4=frases3.split('&')
    frases5=len(frases4) 
    return frases5