def uppCons(frase):
    ''' Dados uma frase retorna a mesma com todas consoantes maíuscilas'''
    i = 0
    nova_frase = ''
    while i < len(frase):
        if frase[i] not in "AEIOUaeiouíÍÌiìãÃéÉ":
            nova_frase+= frase[i].upper()
        else:
            nova_frase+= frase[i]
        i += 1
    return nova_frase