def lingua_p(frase):
    nova = ''
    for x in range(len(frase)):
        if frase[x]=='a' or frase[x]=='e' or frase[x]=='i' or frase[x]=='o' or frase[x]=='u' or frase[x]=='á' or frase[x]=='é' or frase[x]=='í' or frase[x]=='ó' or frase[x]=='ú':
            nova+= frase[x]+'p'+frase[x]
        else:
            nova+=frase[x]
    return nova