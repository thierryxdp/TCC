def inverte(frase):
    ''' função que inverte a ordem do texto, tirando pontuações finais e letra maiuscula inicial
str -> str'''
    frase = frase.replace( ".", " ");
    frase = frase.replace( ",", " ");
    frase = frase.replace( ":", " ");
    frase = frase.replace( ";", " ");
    frase = frase.replace( "!", " ");
    frase = frase.replace( "?", " ");
    frase = frase.replace( "...", " ");
    frase = frase.replace( "-", " ");
    frase = frase.strip()
    frase = frase.lower()
    frase2 = frase.split()
    frase2.reverse()
    frase2 = str.join(" ",frase2)
    return frase2