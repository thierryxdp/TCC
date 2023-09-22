def uppCons(frase):
    nova = ""
    con = "bcçdfghjklmnpqrstvwxyz"
    
    for l in frase:
        if l in con:
            nova += l.upper()
        else:
            nova += l
            
    return nova