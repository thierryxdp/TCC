def uppCons(frase):
    """f"""
    i = 0
    fraseF = ''
    while i < len(frase):
        if frase[i] in 'AEIOUaeiou':
            fraseF = fraseF + str(frase[i].lower)
        i += 1
    return fraseF