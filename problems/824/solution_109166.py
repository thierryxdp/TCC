def uppCons(frase):
    frase=str.split(str.upper((str.join('*',frase))),'*')
    pos=0
    while pos<len(frase):
        if frase[pos] in 'AEIOU,ÃÕÁÉÍÓÚ':
            frase[pos]=str.lower(frase[pos])
        pos=pos+1
    resposta=str.join('',frase)
    return resposta