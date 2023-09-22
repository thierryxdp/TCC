def uppCons(frase):
    f=frase.split(" ")
    i=0
    vogal=''
    while i<len(f):
        if f[i] in "AEIOUaeiou":
            vogal = vogal + f[i]
        if f[i] in "BCDFGHJKLMNPQRSTVXZbcdfghjklmnpqrstvxz,.!?-":
            a=f[i].upper()
            vogal = vogal + a
        i=i+1
    return f