def uppCons(frase):
    """f"""
    i = 0
    fraseF = ''
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiou':
            fraseF = fraseF + str(frase[i].upper)
        i += 1
    return fraseF