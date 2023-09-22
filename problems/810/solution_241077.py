def inverte(frase):
    """dada uma frase retorna a mesma invertida sem letras maiusculas e sem pontuação"""
    frase = fraseAlterada
    fraseAlterada = fraseAlterada.replace('...',' ')
    fraseAlterada = fraseAlterada.replace('.',' ')
    fraseAlterada = fraseAlterada.replace(',',' ')
    fraseAlterada = fraseAlterada.replace('-',' ')
    fraseAlterada = fraseAlterada.replace(';',' ')
    fraseAlterada = fraseAlterada.replace(':',' ')
    fraseAlterada = fraseAlterada.replace('?',' ')
    fraseAlterada = fraseAlterada.replace('!',' ')
    fraseAlterada = fraseAlterada.split
    lista = list.reverse(fraseAlterada)
    phrase = str.join(" ",lista)
    return phrase