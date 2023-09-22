def uppCons(frase):
    i = 0
    while i < len(frase):
        if frase[i] == 'a' or 'e' or 'i' or 'o' or 'u':
            frase  = frase.replace('a','A')
            frase  = frase.replace('e','E')
            frase  = frase.replace('i','I')
            frase  = frase.replace('o','O')
            frase  = frase.replace('u','U')
        i = i + 1
    return frase