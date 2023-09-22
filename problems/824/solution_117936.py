def uppCons(frase):
    maiusculas=0
    i=0
    while i<len(frase):
        if frase[i] in 'QWRTYPSDFGHJKLZXCVBNMaeiou':
            maiusculas=maiusculas+frase[i]
        i+=i+1
    return maiusculas