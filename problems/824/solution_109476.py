def uppCons(frase):
    vog = ['a','e','i','o','u']
    for i in frase:
        if i != vog:
            i.upper()
    return frase