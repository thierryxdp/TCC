def uppCons(frase):
    frase=str.split(str.upper((str.join('*',frase))),'*')
    pos=0
    while pos<len(frase):
        if frase[pos] in 'AEIOU':
            frase[pos]=''
        pos=pos+1
    return frase