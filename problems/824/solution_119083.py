def uppCons(texto):
    fn = " "
    for e in texto:
        if e in 'bcdfghjklmnpqrstvwxyzç':
            fn += str.upper(e)
            else:
                fn += e
                return fn