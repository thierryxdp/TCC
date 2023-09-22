def inverte(frase):
    fraseAlterada = frase
    fraseAlterada = fraseAlterada.replace('.', ' ')
    fraseAlterada = fraseAlterada.replace(',', ' ')
    fraseAlterada = fraseAlterada.replace(';', ' ')
    fraseAlterada = fraseAlterada.replace(':', ' ')
    fraseAlterada = fraseAlterada.replace('-', ' ')
    fraseAlterada = fraseAlterada.replace('!', ' ')
    fraseAlterada = fraseAlterada.replace('?', ' ')
    fraseAlterada = fraseAlterada.replace('...', ' ')
    fraseAlterada2 = str.lower(fraseAlterada)
    fraseAlterada3 = str.split(fraseAlterada2, ' ')
    fraseAlterada4 = fraseAlterada3[::-1]
    fraseAlterada5 = str.join(' ', fraseAlterada4)
    
    return fraseAlterada5