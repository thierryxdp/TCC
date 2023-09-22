def uppCons(frase):
    nova=''
    for letra in frase:
        if letra in 'aeiou':
            nova +=letra.upper()
        else:
            nova += letra
            return nova