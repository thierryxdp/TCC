def uppCons(frase):
    fn = ""
    for e in frase:
        if e in 'bcdfghjklmnpqrstvwxyzç':
            fn += str.upper(e)
        else:
            fn += e
    return fn