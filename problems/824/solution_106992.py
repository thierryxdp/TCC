def uppCons(frase):
    i=0
    while i<len(frase):
        i=i+1
        if 'BCDFGHJKLMNPQRSTVXWYZbcdfghjklmnpqrstvwyz' in frase:
            return str.upper('bcdfghjklmnpqrstvwyz')