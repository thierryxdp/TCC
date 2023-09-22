def uppCons(frase): 
    consoantes="BCDFGJKLMNPQRSTVWXZbcdfgjklmnpqrstvwxz"
    for letra in frase:
        if letra in consoantes:
            consoantes=consoantes.upper()
            return consoantes