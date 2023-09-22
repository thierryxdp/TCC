def uppCons(frase):
    '''eae'''
    i=0
    while i<len(frase):
        if frase[i] != 'aeiouAEIOU':
            frase=frase[i].upper() +i
        if frase[i] == 'aeiou':
            frase=frase[i].lower() +i
        i=i+1
        return frase