def uppCons(frase):
    fn = ""
    for e in frase:
        if e in 'bcdfghjklmnpqrstvwxyz':
            fn += str.upper(e)
        else:
            fn += e
    return fn