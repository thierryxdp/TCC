def uppCons(frases):
    
    P=0
    F=''
    while P<len(frases):
        if frase[P] in 'bcçdfghjklmnpqrstvwwyz':
            F= F+ str.upper(frases[P])
            P+= 1
        else:
            F= F+ frases[P]
            P+= 1
    return F