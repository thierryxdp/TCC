def uppCons(frase):
    novafrase=''
    contadora=0
    while contadora<len(frase):
        letras=frase[contadora]
        if letras in 'bcdfgjklmnpqrstvwxyz':
            letras=str.upper(letras)
        contadora=contadora+1
        novafrase=novafrase+frase[contadora]
    return novafrase