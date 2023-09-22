def inverte(fraseAlterada):
    """dada uma frase retorna a mesma invertida sem letras maiusculas e sem pontuação"""
    
    fraseAlterada = fraseAlterada.replace('...',' ')
    fraseAlterada = fraseAlterada.replace('.',' ')
    fraseAlterada = fraseAlterada.replace(',',' ')
    fraseAlterada = fraseAlterada.replace('-',' ')
    fraseAlterada = fraseAlterada.replace(';',' ')
    fraseAlterada = fraseAlterada.replace(':',' ')
    fraseAlterada = fraseAlterada.replace('?',' ')
    fraseAlterada = fraseAlterada.replace('!',' ')
    fraseAlterada = fraseAlterada.split
    fraseAlterada[::-1]
    str.join(" ",fraseAlterada)
    return fraseAlterada