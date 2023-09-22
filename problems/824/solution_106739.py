def uppCons(frase):
    N = len(frase)
    str1=""
    i=0
    consoantes="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    while i<N:
        if frase[i] in consoantes:
            c = (frase[i]).upper()
            str1=str1+c
        else: str1=str1+frase[i]
        i=i+1   
    return frase