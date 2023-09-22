def uppCons(frase): 
    consoantes="BCDFGJKLMNPQRSTVWXZbcdfgjklmnpqrstvwxz"
    for letra in frase:
        if letra in consoantes:
            consoantes.upper()
    return frase