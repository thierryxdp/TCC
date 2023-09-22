def uppCons(frase):
    s = ''
    for i in frase:
        if i in 'bcdfghjklmnpqrstvxwyzç':
            s += i.upper()
        else:
            s += i