def inverte(frase):
    fraseAlterada = frase
    fraseAlterada = frase.replace('.', ' ')
    fraseAlterada = frase.replace(',', ' ')
    fraseAlterada = frase.replace(';', ' ')
    fraseAlterada = frase.replace(':', ' ')
    fraseAlterada = frase.replace('-', ' ')
    fraseAlterada = frase.replace('!', ' ')
    fraseAlterada = frase.replace('?', ' ')
    fraseAlterada = frase.replace('...', ' ')
    fraseAlterada2 = str.split(fraseAlterada, ' ')
    fraseAlterada3 = str.lower(fraseAlterada2)
    fraseAlterada4 = fraseAlterada3[::-1]
    
    return fraseAlterada4