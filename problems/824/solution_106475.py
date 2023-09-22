def uppCons(frase):
    novafrase=''
    contadora=0
    while contadora<len(frase):
        if frase[contadora] in 'bcdfgjklmnpqrstvwxyz':
            frase[contadora]=list.upper(novafrase)
            novafrase=novafrase+frase[contadora]
            contadora+=1
    return contadora