def uppCons(frase):
    nova = ""
    con = ["bcdfghjklmnpqrstvwxyz"]
    
    for l in frase:
        if l in con:
            nova += l.upper()
        else:
            nova += l
            
    return nova