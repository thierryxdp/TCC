def lingua_p(frase):
    novafrase=''
    for i in frase:
        if str.lower(frase[i])=='aeiou':
            novafrase=novafrase + 'p' + frase[i]
        else:
            novafrase+=frase[i]
    return novafrase