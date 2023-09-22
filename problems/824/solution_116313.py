def uppCons(frase):
    i=0
    cons=''
    while i<len(frase):
        if frase[i] not in "AEIOUaeiou":
            cons=frase[i].upper()
        i=i+1
    return cons