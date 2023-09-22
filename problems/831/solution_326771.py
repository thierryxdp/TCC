def lingua_p(frase):
    novafrase=''
    for i in range(0,len(frase)):
        if str.lower(frase[i]) in 'aeiou':
            novafrase+='p' + frase[i]
        else:
            novafrase+=frase[i]
    return novafrase