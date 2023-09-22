def lingua_p(x):
    '''retorna uma palavra qualquer (x) em portugues traduzida para a lingua do p.str,str->str'''
    y = str()
    for w in x:
        if w in "aoieuéáàúíó":
            y+= w + 'p' + w
        if w not in "aoieuéáàúíó":
            y+= w
            
            
    return y