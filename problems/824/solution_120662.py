def uppCons(frase):
    proximo = 0
    while proximo < len(frase):
        if 'a' in frase:
            frase.replace('a','A')
        if 'e' in frase:
            frase.replace('e','E')
        if 'i' in frase:
            frase.replace('i','I')
        if 'o' in frase:
            frase.replace('o','O')
        if 'U' in frase:
            frase.replace('u','U')
    return frase