def uppCons (string):
    '''isando o while para percorrer a listas, depois
    retirando qualquer variação de consoantes'''
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