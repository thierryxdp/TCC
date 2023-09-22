def uppCons(frase):
    i=0
    while i<len(frase):
        i=i+1
        if 'AEIOUaeiou' in frase:
            return frase
        if 'BCDFGHJKLMNPQRSTVXWYZ,bcdfghjklmnpqrstvwyz' in frase:
            return str.upper(''BCDFGHJKLMNPQRSTVXWYZ,bcdfghjklmnpqrstvwyz')