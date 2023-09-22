def uppCons (string):
    frase=""
    i=0
    while i<len(string):
        if string[i] not in"aeiouAEIOUáéíóúÁÉÍÓÚãõÃÕ":
            frase+= string[i].upper()
            i+=1
        else:
            frase+=string[i]
            i+=1
    return frase