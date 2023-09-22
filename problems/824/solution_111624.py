def uppCons(frase):
    """ """
    i=0
    cons=""
    while i<len(frase):
        if frase[i]not in "AEIOUaeiou":
            cons=cons+frase[i]
        i=i+1

    return cons