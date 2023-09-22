def uppCons(frase): 
    consoantes="BCDFGJKLMNPQRSTVWXZbcdfgjklmnpqrstvwxz"
    for letra in frase:
        if letra in consoantes:
            frase.upper()
        return frase