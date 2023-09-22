def uppCons(frase):
    """ """
    consoantes="b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","ç"
    while indice<len(frase):
        if frase[indice] in consoantes:
            frase[indice].upper()
            indice +=1
        return frase