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
    'lista' = fraseAlterada[::-1]
    phrase = str.join(" ",Lista)
    return phrase