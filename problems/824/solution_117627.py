def uppCons(frase):
    ora=''
    i=0
    while i<(len(frase)):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            ora=ora+str.upper()
        else:
            ora=ora+caractere
        i=i+1
    return ora