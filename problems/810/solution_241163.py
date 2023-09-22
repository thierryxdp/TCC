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
    fraseAlterada2 = str.lower(fraseAlterada)
    fraseAlterada3 = fraseAlterada2[::-1]
    
    return fraseAlterada3