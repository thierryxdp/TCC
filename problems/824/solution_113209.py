def uppCons(frase):
    i=0
    vogal=''
    while i<len(frase):
        if frase[i] in "AEIOUaeiou":
            vogal = vogal + frase[i]
        i=i+1
    return vogal