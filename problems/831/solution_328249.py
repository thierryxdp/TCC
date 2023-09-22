def lingua_p(x):
    '''retorna uma palavra qualquer (x) em portugues traduzida para a lingua do p.str,str->str'''
    y = str()
    for w in x:
        if w in "aoieuéáàúíó":
            y+= str(w) + 'p' + str(w)
        if w not in "aoieuéáàúíó":
            y+= str(w)
            
            
    return y