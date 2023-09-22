def uppCons(frase):
    fn = ""
    for e in frase:
        if e in 'bcdfghijklmnpqrstvwxyzç':
            fn += str.upper(e)
        else:
            fn += e
        return fn