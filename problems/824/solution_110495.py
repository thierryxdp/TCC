def uppCons(frase):
    ''''''
    fraseN = ''
    i=0
    while i<len(frase):
        if 'AEIOUaeiou' in frase:
            fraseN= fraseN + frase[i]
            i=i+1
        else:
            fraseN= fraseN + str.upper(frase[i])
            i=i+1    
    return fraseN