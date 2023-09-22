def uppCons(frase):
    ora=''
    i=0
    while i<(len(frase)):
        if frase[i] in 'bcdfghjklmnpqrstvxwyzç':
            ora=ora+str.upper(frase[i])
        else:
            ora=ora+frase[i]
        i=i+1
    return ora