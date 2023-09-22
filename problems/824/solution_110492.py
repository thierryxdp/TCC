def uppCons(frase):
    ''''''
    fraseN = ''
    i=0
    while i<len(palavra):
        if 'AEIOUaeiou' in frase:
            fraseN=fraseN + frase[i]
        i=i+1
        if 'AEIOUaeiou' not in frase:
            fraseN=fraseN + str.upper(frase[i])
    return fraseN