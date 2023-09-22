def uppCons(frase):
    i=0
    vogal=''
    while i<len(frase):
        if frase[i] in "AEIOUaeiou":
            vogal = vogal + frase[i]
        if frase[i] in "BCDFGHJKLMNPQRSTVXZbcdfghjklmnpqrstvxz,.!?-":
            a=frase[i].upper()
            vogal = vogal + a
        i=i+1
    return