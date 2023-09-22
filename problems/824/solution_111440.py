def uppCons(frase):
    i=0
    a=len(frase)
    vogais='AEIOUaeiouãéíóú'
    while i<a:
        if frase[i] not in vogais:
            frase=list(frase)
            frase[i]=str.upper(frase[i])
            frase=str.join('',frase)
        i=i+1
    return frase