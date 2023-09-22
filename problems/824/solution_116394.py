def uppCons(frase):
    i=0
    novo=str.upper(frase)
    while i<len(novo):
        if novo[i] in 'AEIOU':
            frase=str.replace(novo,novo[i],str.lower(novo[i]))     
        i+=1
    return frase