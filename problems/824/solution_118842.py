def uppCons(frase):
    minuscula = "bcçdfghjklmnpqrstvwxyz"
    maiuscula = "BCÇDFGHJKLMNPQRSTVWXYZ"
    traducao = str.maketrans(minuscula, maiuscula)
    return frase.translate(traducao)