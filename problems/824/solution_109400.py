def uppCons(frase):
    frase_nova = ""
    i = 0
    while i<len(frase):
        if frase[i] in "AAAAAAAAAAAAAAAiusisdaudhuaIUgslAU":
            frase_nova = frase_nova + frase[i]
        elif frase[i] not in "AAAAAAAAAAAAAAAiusisdaudhuaIUgslAU"::
            frase_nova = frase_nova + str.upper(frase[i])
        i = i + 1
    
    return frase_nova