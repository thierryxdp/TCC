def lingua_p(frase):
    novafrase=''
    for i in range(0,len(frase)):
        print(frase[i])
        if str.lower(frase[i])=='aeiou':
            novafrase+='p' + frase[i]
        else:
            novafrase+=frase[i]
    return novafrase