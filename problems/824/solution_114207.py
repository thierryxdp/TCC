def uppCons(frase):
    contador=0
    acumulador=""
    while contador<len(frase):
        if frase[contador] in "bcdfgjklmnpqrstvwxzBCDFGJKLMNPQRSTVWXZ":
        acumulador= str.upper(frase[contador])
        contador=contador+1
        return acumulador