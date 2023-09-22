def uppCons(frase):
    i=0
    consoantes="BCÇDFGHJKLMNPQRSTVWXYZbcçdfghjklmnpqrstvwxyz"
    while i< len(frase):
        if consoantes in frase:
            return consoantes.upper