def lingua_p(frase):
    '''Dada uma frase, retorna com ela traduzida para a língua do P.
    str -> str'''
    nova = ''
    for x in range(len(frase)):
        if frase[x]=='a' or frase[x]=='e' or frase[x]=='i' or frase[x]=='o' or frase[x]=='u':
            nova+= frase[x]+'p'+frase[x]
        else:
            nova+=frase[x]
    return nova