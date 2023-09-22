def uppCons(frase):
    '''eae'''
    i=2
    while i<len(frase):
        if frase[i] != 'aeiouAEIOU':
            frase=frase[i].upper()
        if frase[i] == 'aeiou':
            frase=frase[i].lower()
        i=i+1
        return frase