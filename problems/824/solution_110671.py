def uppCons(frase):
    '''...'''
    i = 0
    frase1 = ''
    while i < len(frase):
        if (frase[i]) not in 'aeiouàáãâèéêìíîòóôõùúû':
            frase1 = frase1 + frase[i].upper()
            else:
                frase1 = frase1 + frase[i].lower()
                i = i + 1
                return frase1