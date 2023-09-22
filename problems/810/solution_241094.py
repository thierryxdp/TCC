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
    str.split(fraseAlterada,',')
    str.join(" ",fraseAlterada)
    fraseAlterada[::-1]
    return fraseAlterada