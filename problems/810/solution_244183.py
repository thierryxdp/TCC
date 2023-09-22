def substitui_pontuação(texto):
    ''' '''
    mod = str.replace(texto,'.',' ')
    mod = str.replace(mod,'...',' ')
    mod = str.replace(mod,'!',' ')
    mod = str.replace(mod,'?',' ')
    mod = str.replace(mod,',',' ')
    mod = str.replace(mod,'-',' ')
    mod = str.replace(mod,';',' ')
    mod = str.replace(mod,':',' ')
    return mod

def inverte(frase):
    mod = substitui_pontuação(frase)
    mod = str.split(mod)
    list.reverse(mod)
    mod = str.join(' ',mod)
    return mod