def uppCons(frase):
    novafrase=''
    contadora=0
    while contadora<len(frase):
        letras=frase[contadora]
        if letras in 'bcdfgjklmnpqrstvwxyz':
            letras=str.upper(novafrase)
            novafrase=novafrase+frase[contadora]
            contadora+=1
    return novafrase