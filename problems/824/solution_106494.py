def uppCons(frase):
    novafrase=''
    contadora=0
    while contadora<len(frase):
        letras=frase[contadora]
        if letras in 'bcdfghjklmnpqrstvwxyz':
            letras=str.upper(letras)
        contadora=contadora+1
        novafrase=novafrase+letras
    return novafrase