def consoanteMaiuscula(x):
    if x not in "aeiouáéíóúàèìòùâêîôûãẽĩõũ":
        return x.upper()
    return x

def uppCons(frase):
    return "".join(list(map(consoanteMaiuscula, frase)))