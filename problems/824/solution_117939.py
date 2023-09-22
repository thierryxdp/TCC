def uppCons(frase):
    maiusculas=''
    i=0
    while i<len(frase):
        if frase[i] in 'QWRTYPSDFGHJKLZXCVBNMAEIOUaeiou':
            maiusculas=maiusculas+frase[i]
        i+=i+1
    return maiusculas