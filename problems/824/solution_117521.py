def uppCons(frase):
    #posição= P
    P=0
    frase_final=''
    while P<len(frase):
        if frase[P] not in 'aeiou':
            frase_final= frase_final+ str.upper(frase[P])
            P+= 1
        else:
            frase_final= frase_final+ frase[P]
            P+= 1
    return frase_final