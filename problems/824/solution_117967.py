def consoanteMaiuscula(x):
    if x not in "aeiou":
        return x.upper()
    return x

def uppCons(frase):
    return list(map(consoanteMaiuscula, frase))