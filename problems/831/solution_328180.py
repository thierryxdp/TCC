def lingua_p(frase):
    frasep=[]
    for l in frase:
        if l in "aeiouAEIOU":
            frasep.append(l.lower()+"p"+l.lower())
        else:
            frasep.append(l.lower())
    return "".join(frasep)