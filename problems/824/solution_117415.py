def uppCons(frase):
    #posição= P
    P=0
    F=''
    while P<len(frase):
        if frase[P] in 'bcçdfghjklmnpqrstvwwyz':
            F= F+ str.upper(frase[P])
            P+= 1
        else:
            F= F+ frase[P]
            P+= 1
    return F